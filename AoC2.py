f = open("input3.txt","r")

arr = []
for l in f.readlines():
    arr.append(l)


length = 31
print(arr)

nums = [(1,1),(3,1),(5,1),(7,1),(1,2)]
sol = 1
for ent in nums:
    count=0
    a=ent[1]
    b=ent[0]
    for i in range(len(arr)):
        if a*i < len(arr):
            if arr[a*i][(b*i)%length] == "#":
                count += 1
            #arr[i][(3*i)%l] = "X"
        #else:
            #arr[i][(3*i)%l] = "O"
    sol *= count
    print(count)
print(sol)
