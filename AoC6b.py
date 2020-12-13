f = open('input7.txt','r')
sum = [0]
def dfs(curr_bag, connections, curr_factor, sum):
    #visited.append(curr_bag)
    if curr_bag in connections.keys():
        for b in connections[curr_bag].keys():

            new_factor = curr_factor*connections[curr_bag][b]
            sum[0] += new_factor
            dfs(b,connections,new_factor,sum)

    #else:
        #visited[curr_bag] = True

visited = []
connections = {}
for l in f.readlines():

    l2 = l[:-2]
    line = l2.split("bags")
    base = line[0]+"bags"
    line = l2.split(" ")
    chopline = line[3:]
    nextbags = {}
    print(base + " : " + str(chopline))
    for i in range(len(chopline)):
        if 'bag' in chopline[i]:
            if chopline[i-1] == 'other':
                continue
            nextbag = chopline[i-2]+" "+chopline[i-1]+" bags"
    #        visited[nextbag] = False
            nextbags[nextbag] = int(chopline[i-3])
            # if nextbag in connections.keys():
            #     (connections[nextbag]).append(base)
            # else:
            #     connections[nextbag] = [base]
    if len(nextbags)>0:
        connections[base] = nextbags

dfs('shiny gold bags',connections,1,sum)
# for k in visited:
#     if k in visited:
#         counter += 1
print(sum[0])
