# f = open('input13.txt','r')
#
# buses = []
# t_0 = int(f.readline()[:-1])
# for i in (f.readline()[:-1]).split(','):
#     if i == 'x':
#         continue
#     buses.append(int(i))
# t = t_0
# dt = 2*t_0
# bus = -1
# found = False
# while True:
#     for b in buses:
#         if t%b == 0:
#             print(b*(t-t_0))
#             found = True
#             break
#     if found:
#         break
#     t += 1


f = open('input13.txt','r')

buses = []
f.readline()
t_0 = 100000000000011
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
    t += 23
