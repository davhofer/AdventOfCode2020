f = open('input7.txt','r')


dict = {}

for l in f.readlines():
    dict[l.split(" contain ")[0]] = l.split(" contain ")[1]


reachables = []
def brute(cur,lines,reachables):
    for k in lines.keys():
        if cur in lines[k]:
            if k not in reachables:
                reachables.append(k)
                brute(k,lines,reachables)

brute('shiny gold bags',lines,reachables)

print(len(reachables))
