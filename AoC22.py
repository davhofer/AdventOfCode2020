import queue
f = open('test22_b.txt','r')
q1 = queue.SimpleQueue()
q2 = queue.SimpleQueue()

f.readline()
l = f.readline()
while len(l) > 1:
    q1.put(int(l))
    l = f.readline()
print(f.readline())
l = f.readline()
while len(l) > 1:
    q2.put(int(l))
    l = f.readline()

print(q1.qsize())
print(q2.qsize())


def copyQ(q):
    newq = queue.SimpleQueue()
    n = q.qsize()
    for i in range(n):
        x = q.get()
        q.put(x)
        newq.put(x)
    return newq

def copyQl(q,l):
    newq = queue.SimpleQueue()
    n = q.qsize()
    for i in range(n):
        x = q.get()
        q.put(x)
        if i < l:
            newq.put(x)
    return newq

def recursiveCombat(q1,q2,d):
    #print(d)
    snaps = []
    while q1.qsize() > 0 and q2.qsize() > 0:
        q1c = copyQ(q1)
        q2c = copyQ(q2)
        a1 = []
        a2 = []
        for i in range(q1.qsize()):
            a1.append(q1c.get())
        for i in range(q2.qsize()):
            a2.append(q2c.get())
        prev = False
        for s in snaps:
            if len(s[0]) == len(a1) and len(s[1]) == len(a2):
                first = True
                second = True
                for i in range(len(a1)):
                    if a1[i] != s[0][i]:
                        first = False
                for i in range(len(a2)):
                    if a2[i] != s[1][i]:
                        second = False
                if first and second:
                    prev = True
                    break
        if prev:
            # player 1 wins
            return "1"
        else:
            snaps.append([a1,a2])

        a = q1.get()
        b = q2.get()
        if q1.qsize() >= a and q2.qsize() >= b:
            roundW = recursiveCombat(copyQl(q1,a),copyQl(q2,b),d+1)
        else:
            if a > b:
                roundW = "1"
            else:
                roundW = "2"

        if roundW == "1":
            q1.put(a)
            q1.put(b)
        else:
            q2.put(b)
            q2.put(a)
    if q1.qsize() > 0:
        return "1"
    else:
        return "2"
w = recursiveCombat(q1,q2,0)

if w == "1":
    assert q1.qsize()>0 and q2.qsize() == 0
    winner = q1
else:
    assert q2.qsize()>0 and q1.qsize() == 0
    winner = q2
#
# if not w:
#     if q1.qsize() > 0:
#         winner = q1
#     else:
#         winner = q2

ans = 0
for i in range(winner.qsize(),0,-1):
    ans += winner.get()*i
print(ans)
