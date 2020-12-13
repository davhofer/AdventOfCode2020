f = open('input7.txt','r')

def dfs(curr_bag, connections, visited):
    visited[curr_bag] = True
    for b in connections[curr_bag]:
        if not visited[b]:
            dfs(b,connections,visited, counter)

visited = {}
can_reach = []
connections = {}
for l in f.readlines():
    l2 = l[:-2]
    line = l2.split("bags")
    base = line[0]+"bags"
    line = l2.split(" ")
    chopline = line[3:]
    nextbags = []
    visited[base] = False
    for i in range(len(chopline)):
        if chopline[i] == "bags":
            if chopline[i-1] == 'other':
                continue
            nextbag = chopline[i-2]+" "+chopline[i-1]+" "+chopline[i]
            visited[nextbag] = False
            nextbags.append(nextbag)
        elif chopline[i] == "bags,":
            if chopline[i-1] == 'other':
                continue
            nextbag = chopline[i-2]+" "+chopline[i-1]+" "+chopline[i][:-1]
            visited[nextbag] = False
            nextbags.append(nextbag)
        elif chopline[i] == "bag":
            if chopline[i-1] == 'other':
                continue
            nextbag = chopline[i-2]+" "+chopline[i-1]+" "+chopline[i]+"s"
            visited[nextbag] = False
            nextbags.append(nextbag)
    connections[base] = nextbags

keys = visited.keys()
for b in keys:
    if not visited[b]:
        print("Started dfs from " + b)
        dfs(b,connections,visited,counter)

print(counter[0])
