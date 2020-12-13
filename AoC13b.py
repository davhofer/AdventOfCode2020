def GCD(x, y):

   while(y):
       x, y = y, x % y

   return x
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

f = open('input13.txt','r')

equations = []
f.readline()
l = f.readline().split(',')
for i in range(len(l)):
    if l[i] == 'x':
        continue
    else:
        equations.append([(0-i)%int(l[i]),int(l[i])])
print(equations)
n = len(equations)
factors =[1]*n


for i in range(n):
    for j in range(n):
        if i == j:
            continue
        factors[j] *= equations[i][1]


for i in range(n):
    print(modinv(factors[i],equations[i][1]))
    factors[i] = factors[i] * modinv(factors[i],equations[i][1])* equations[i][0]
print(factors)
sum = 0
for f in factors:
    sum += f

ff = 1
for e in equations:
    ff *= e[1]

print(sum%ff)
