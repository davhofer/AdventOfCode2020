f = open('test21.txt','r')
raw_ingr = []
raw_aller = []
A = {}
for l in f.readlines():
    line = l[:-1]
    ingr = line.split(' (contains ')[0]
    aller = line.split(' (contains ')[1][:-1]
    ingr = ingr.split(' ')
    aller = aller.split(', ')
    for a in aller:
        if a not in A.keys():
            A[a] = [set(ingr)]
        else:
            A[a].append(set(ingr))
    raw_ingr.append(ingr)
    raw_aller.append(aller)
blocked = set([])

assignd = {}
A_int = {}
max = 0
for a in A.keys():
    ingr = A[a]
    inters = ingr[0].intersection(*A[a])

    if len(inters) == 1:
        assignd[a] = inters
    else:
        A_int[a] = inters
    if len(inters) > max:
        max = len(inters)
    blocked = blocked.union(inters)

while len(A_int.keys()) > 0:
    print(A_int)
    newA = {}
    for a in A_int.keys():
        for x in assignd.keys():
            if next(iter(assignd[x])) in A_int[a]:
                A_int[a] = A_int[a]-assignd[x]
        if len(A_int[a]) > 1:
            newA[a] = A_int[a]
        else:
            assignd[a] = A_int[a]
    A_int = newA


print(assignd)
print(max)
count = 0
print(blocked)


for l in raw_ingr:
    for x in l:
        if x not in blocked:
            count += 1
print(count)

lastlist = []
for k in assignd.keys():
    lastlist.append(k)

lastlist = sorted(lastlist)

ans = ''
for x in lastlist:
    ans+=next(iter(assignd[x]))+','
ans = ans[:-1]
print(ans)
    # inters = set(ingr[0])
    # for i in ingr:
    #     inters = inters.intersection(set(i))
