f = open('input16.txt','r')

ranges = []
l = f.readline()
while len(l) > 1:
    a = (l.split(':')[1]).split(' or ')[0]
    b = (l.split(':')[1]).split(' or ')[1]
    ranges.append([ range( int(a.split('-')[0]) , int(a.split('-')[1])+1 ),
    range(int(b.split('-')[0]) , int(b.split('-')[1])+1) ])
    l = f.readline()

f.readline()
y_ticket = []
for x in f.readline().split(','):
    y_ticket.append(int(x))

tickets = []

f.readline()
f.readline()
l = f.readline()
while len(l) > 1:
    t = []
    for x in l.split(','):
        t.append(int(x))
    tickets.append(t)
    l = f.readline()

valid_tickets = []
invalids = []
for t in tickets:
    t_valid = True
    for v in t:
        valid = False
        for r in ranges:
            if v in r[0] or v in r[1]:
                valid = True
        if not valid:
            t_valid = False
            invalids.append(v)
    if t_valid:
        valid_tickets.append(t)
valid_tickets.append(y_ticket)
sum = 0
for x in invalids:
    sum += x
print(sum)

sums = []
positions = {}
assignment = {}
for i in range(len(ranges)):
    mask = [1]*len(ranges)
    for t in valid_tickets:
        for r in range(len(ranges)):
            if t[i] not in ranges[r][0] and t[i] not in ranges[r][1]:
                mask[r] = 0
    s = 0
    for x in mask:
        s += x
    sums.append(s)
    if s in assignment.keys():
        print("KEY ERROR")
    assignment[s] = [i,mask]
    print(mask)

for i in range(len(ranges)):
    for j in range(len(ranges)):
        if assignment[i+1][1][j] == 1 and j not in positions.values():
            positions[assignment[i+1][0]] = j
ans = 1
print(positions)
for i in positions.keys():
    if positions[i] < 6:
        ans *= y_ticket[i]
print(ans)
