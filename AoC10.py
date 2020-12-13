f = open('input10.txt','r')
v = [0]
for l in f.readlines():
    v.append(int(l[:-1]))
list.sort(v)

curr = 0
diff_1 = 0
diff_3 = 0
for i in range(len(v)):
    if v[i]-curr == 3:
        diff_3 += 1
    elif v[i]-curr == 1:
        diff_1 += 1
    curr = v[i]
diff_3 += 1
print(diff_1*diff_3)

N = (v[-1]+1)
v.append(N)
DP = [0]*(N)
DP[0] = 1
DP[1] = 1
DP[2] = 2
for i in range(3,N):
    if i in v:
        DP[i] = DP[i-1] + DP[i-2] + DP[i-3]
print(DP)
