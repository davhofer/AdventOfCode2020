def count_neighbors(x,y,z,o,active):
    s = 0
    for i in range(x-1,x+2):
        for j in range(y-1,y+2):
            for k in range(z-1,z+2):
                for l in range(o-1,o+2):
                    if i == x and j == y and k == z and l == o:
                        continue
                    if (i,j,k,l) in active.keys():
                        s +=1
    return s

f = open('input17.txt','r')

base = (6,6,10,10)

active = {}
next_active = {}
x = 6
y = 6
z = 10
o = 10
for l in f.readlines():
    x = 6
    for i in range(len(l)):
        if l[i] == '#':
            active[(x,y,z,o)] = 1
            print((x,y,z,o))
        x += 1
    y += 1

x_0 = 6
x_1 = 14
y_0 = 6
y_1 = 14
z_1 = 10
z_0 = 10
o_0 = 10
o_1 = 10


for i in range(6):

    x_0 -= 1
    y_0 -= 1
    z_0 -= 1
    x_1 += 1
    y_1 += 1
    z_1 += 1
    o_0 -= 1
    o_1 += 1

#my_dict.pop('key', None)
    for x in range(x_0,x_1+1):
        for y in range(y_0,y_1+1):
            for z in range(z_0,z_1+1):
                for o in range(o_0,o_1+1):
                #print((x,y,z))

                    n = count_neighbors(x,y,z,o,active)
                    #print(n)
                    alive = ((x,y,z,o) in active.keys())
                    #print(alive)
                    if alive and n == 2 or n == 3:
                        #active.pop((x,y,z), None)
                        next_active[(x,y,z,o)] = 1
                    elif not alive and n == 3:
                        print("new cell")
                        next_active[(x,y,z,o)] = 1

    active = next_active
    next_active = {}
    print(len(active.keys()))



print(len(active.keys()))
