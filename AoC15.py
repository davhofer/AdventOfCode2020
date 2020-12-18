#f = open('input15.txt','r')
num = [18,11,9,0,5,1]
speak = 0
last = 0
n0 = len(num)
for i in range(30000000-n0):
    last = num[-1]
    if last not in num[:-1]:
        speak = 0
    else:
        for j in range(len(num)-2,-1,-1):
            if num[j] == last:
                speak = len(num)-j-1
                break
    num.append(speak)
print(speak)
