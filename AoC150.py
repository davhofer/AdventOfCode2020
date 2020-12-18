#f = open('input15.txt','r')
start = [18,11,9,0,5]
d = {}
for i in range(len(start)):
    d[start[i]] = i
speak = 0
last = 1
n0 = len(start)
for i in range(n0+1,30000000):
    if last not in d.keys():
        speak = 0
    else:
        speak = i-d[last]-1
    d[last] = i-1
    last = speak
    #print(speak)
print(speak)
