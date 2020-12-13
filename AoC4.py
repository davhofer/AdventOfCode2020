f = open("input5.txt","r")
import math

n = 128*9

ids = [0]*n

maxID = 0
for l in f.readlines():
    bot = 0
    top = 127
    mid = math.floor((top-bot)/2)
    for i in range(7):
        if l[i] == "F":
            top = mid
            mid = bot+math.floor((top-bot)/2)
        if l[i] == "B":
            bot = mid+1
            mid = bot+math.floor((top-bot)/2)
    row = mid
    bot = 0
    top = 7
    mid = math.floor((top-bot)/2)
    for i in range(3):
        if l[7+i] == "L":
            top = mid
            mid = bot+math.floor((top-bot)/2)
        if l[7+i] == "R":
            bot = mid+1
            mid = bot+math.floor((top-bot)/2)
    col = mid
    id = row*8+col

    ids[id] = ids[id] + 1
    if id > maxID:
        maxID = id

print(maxID)
print(ids)
for i in range(1,128*9-2):
    if ids [i] == 0 and ids[i+1] > 0 and ids[i-1] > 0:
            col = i%8
            row = math.floor((i-col)/8)
            print(i)
            print(str(row)+", "+str(col))
