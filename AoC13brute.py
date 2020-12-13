import time
start = int(round(time.time() * 1000))

f = open('input13.txt','r')

buses = []
f.readline()
t_0 = 100000000000126-23
l = f.readline().split(',')
for i in range(len(l)):
    if l[i] == 'x':
        continue
    else:
        buses.append([int(l[i]),i])
t = t_0
while True:
    valid = True
    for i in range(len(buses)):
        if (t+buses[i][1])%buses[i][0] != 0:
            valid = False
            #print(t)
            break
    if valid:
        print("Solution = " + str(t))
        break
    t += 733




stop = int(round(time.time() * 1000))
print("time: " + str(start-stop) + " ms")
