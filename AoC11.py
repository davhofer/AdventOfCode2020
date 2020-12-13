f = open('input11.txt','r')

def getseat(seats,pos,dir):
    x = pos[0]+dir[0]
    y = pos[1]+dir[1]
    seat = seats[x][y]
    while seat == '.' and x+dir[0] >= 0 and x+dir[0] <= len(seats)-1 and y+dir[1] >= 0 and y+dir[1] <= len(seats[0])-1:
        x += dir[0]
        y += dir[1]
        seat = seats[x][y]
    return seat


seats = []
for l in f.readlines():
    seats.append(l[:-1])

n = len(seats[0])
m = len(seats)

print(m)
changed = True
c = 0
while changed:
    if c < 4:
        for asdf in seats:
            print(asdf)
        print('----------------------------------------------')
    c += 1

    changed = False
    newSeats = []
    globalOcc = 0

    l1 = ''
    #corner seat
    if seats[0][0] == '.':
        l1 += '.'
    elif seats[0][0] == 'L':
        if getseat(seats,[0,0],[0,1]) != '#' and getseat(seats,[0,0],[1,1]) != '#' and getseat(seats,[0,0],[1,0]) != '#':
            l1 += '#'
            globalOcc += 1
            changed = True
        else:
            l1 += 'L'
    elif seats[0][0] == '#':
        l1 += '#'
        globalOcc += 1
    #first line
    for i in range(1,n-1):
        if seats[0][i] == '.':
            l1 += '.'
        elif seats[0][i] == 'L':
            if getseat(seats,[0,i],[0,-1]) != '#' and getseat(seats,[0,i],[1,-1]) != '#' and getseat(seats,[0,i],[1,0]) != '#' and seats[1][i+1] != '#' and seats[0][i+1] != '#':
                l1 += '#'
                globalOcc += 1
                changed = True
            else:
                l1 += 'L'
        elif seats[0][i] == '#':
            occ = 0
            if getseat(seats,[0,i],[0,-1]) == '#':
                occ += 1
            if getseat(seats,[0,i],[1,-1]) == '#':
                occ += 1
            if getseat(seats,[0,i],[1,0]) == '#':
                occ += 1
            if getseat(seats,[0,i],[1,1]) == '#':
                occ += 1
            if getseat(seats,[0,i],[0,1]) == '#':
                occ += 1
            if occ >= 5:
                l1 += 'L'
                changed = True
            else:
                l1 += '#'
                globalOcc += 1
    #corner seat 2
    if seats[0][n-1] == '.':
        l1 += '.'
    elif seats[0][n-1] == 'L':
        if getseat(seats,[0,n-1],[0,-1]) != '#' and getseat(seats,[0,n-1],[1,-1]) != '#' and getseat(seats,[0,n-1],[1,0]) != '#':
            l1 += '#'
            globalOcc += 1
            changed = True
        else:
            l1 += 'L'
    elif seats[0][n-1] == '#':
        l1 += '#'
        globalOcc += 1

    newSeats.append(l1)





    for i in range(1,m-1):
        newl = ''

        #leftmost seat
        if seats[i][0] == '.':
            newl += '.'
        elif seats[i][0] == 'L':
            if getseat(seats,[i,0],[-1,0]) != '#' and getseat(seats,[i,0],[-1,1]) != '#' and getseat(seats,[i,0],[0,1]) != '#' and getseat(seats,[i,0],[1,1]) != '#' and getseat(seats,[i,0],[1,0]) != '#':
                newl += '#'
                globalOcc += 1
                changed = True
            else:
                newl += 'L'
        elif seats[i][0] == '#':
            occ = 0
            if getseat(seats,[i,0],[-1,0]) == '#':
                occ += 1
            if getseat(seats,[i,0],[-1,1]) == '#':
                occ += 1
            if getseat(seats,[i,0],[0,1]) == '#':
                occ += 1
            if getseat(seats,[i,0],[1,1]) == '#':
                occ += 1
            if getseat(seats,[i,0],[1,0]) == '#':
                occ += 1
            if occ >= 5:
                newl += 'L'
                changed = True
            else:
                newl += '#'
                globalOcc += 1
        # loop
        for j in range(1,n-1):
            if seats[i][j] == '.':
                newl += '.'
            elif seats[i][j] == 'L':
                if getseat(seats,[i,j],[-1,0]) != '#' and getseat(seats,[i,j],[-1,1]) != '#' and getseat(seats,[i,j],[0,1]) != '#' and getseat(seats,[i,j],[1,1]) != '#' and getseat(seats,[i,j],[1,0]) != '#' and getseat(seats,[i,j],[1,-1]) != '#' and getseat(seats,[i,j],[0,-1]) != '#' and getseat(seats,[i,j],[-1,-1]) != '#':
                    newl += '#'
                    globalOcc += 1
                    changed = True
                else:
                    newl += 'L'
            elif seats[i][j] == '#':
                occ = 0
                if getseat(seats,[i,j],[-1,0]) == '#':
                    occ += 1
                if getseat(seats,[i,j],[-1,1]) == '#':
                    occ += 1
                if getseat(seats,[i,j],[0,1]) == '#':
                    occ += 1
                if getseat(seats,[i,j],[1,1]) == '#':
                    occ += 1
                if getseat(seats,[i,j],[1,0]) == '#':
                    occ += 1
                if getseat(seats,[i,j],[1,-1]) == '#':
                    occ += 1
                if getseat(seats,[i,j],[0,-1]) == '#':
                    occ += 1
                if getseat(seats,[i,j],[-1,-1]) == '#':
                    occ += 1
                if occ >= 5:
                    newl += 'L'
                    changed = True
                else:
                    newl += '#'
                    globalOcc += 1
        #rightmost seat
        if seats[i][n-1] == '.':
            newl += '.'
        elif seats[i][n-1] == 'L':
            if getseat(seats,[i,n-1],[-1,0]) != '#' and getseat(seats,[i,n-1],[-1,-1]) != '#' and getseat(seats,[i,n-1],[0,-1]) != '#' and getseat(seats,[i,n-1],[1,-1]) != '#' and getseat(seats,[i,n-1],[1,0]) != '#':
                newl += '#'
                globalOcc += 1
                changed = True
            else:
                newl += 'L'
        elif seats[i][n-1] == '#':
            occ = 0
            if getseat(seats,[i,n-1],[-1,0]) == '#':
                occ += 1
            if getseat(seats,[i,n-1],[-1,-1]) == '#':
                occ += 1
            if getseat(seats,[i,n-1],[0,-1]) == '#':
                occ += 1
            if getseat(seats,[i,n-1],[1,-1]) == '#':
                occ += 1
            if getseat(seats,[i,n-1],[1,0]) == '#':
                occ += 1
            if occ >= 5:
                newl += 'L'
                changed = True
            else:
                newl += '#'
                globalOcc += 1
        newSeats.append(newl)

    lm = ''
    #corner seat
    if seats[m-1][0] == '.':
        lm += '.'
    elif seats[m-1][0] == 'L':
        if getseat(seats,[m-1,0],[0,1]) != '#' and getseat(seats,[m-1,0],[-1,1]) != '#' and getseat(seats,[m-1,0],[-1,0]) != '#':
            lm += '#'
            globalOcc += 1
            changed = True
        else:
            lm += 'L'
    elif seats[m-1][0] == '#':
        lm += '#'
        globalOcc += 1
    #last line
    for i in range(1,n-1):
        if seats[m-1][i] == '.':
            lm += '.'
        elif seats[m-1][i] == 'L':
            if getseat(seats,[m-1,i],[0,1]) != '#' and getseat(seats,[m-1,i],[-1,1]) != '#' and getseat(seats,[m-1,i],[-1,0]) != '#' and getseat(seats,[m-1,i],[-1,-1]) != '#' and getseat(seats,[m-1,i],[0,-1]) != '#':
                lm += '#'
                globalOcc += 1
                changed = True
            else:
                lm += 'L'
        elif seats[m-1][i] == '#':
            occ = 0
            if getseat(seats,[m-1,i],[0,1]) == '#':
                occ += 1
            if getseat(seats,[m-1,i],[-1,1]) == '#':
                occ += 1
            if getseat(seats,[m-1,i],[-1,0]) == '#':
                occ += 1
            if getseat(seats,[m-1,i],[-1,-1]) == '#':
                occ += 1
            if getseat(seats,[m-1,i],[0,-1]) == '#':
                occ += 1
            if occ >= 5:
                lm += 'L'
                changed = True
            else:
                lm += '#'
                globalOcc += 1
    #corner seat 2 CONTINUE HERE
    if seats[m-1][n-1] == '.':
        lm += '.'
    elif seats[m-1][n-1] == 'L':
        if getseat(seats,[m-1,n-1],[0,-1]) != '#' and getseat(seats,[m-1,n-1],[-1,-1]) != '#' and getseat(seats,[m-1,n-1],[-1,0]) != '#':
            lm += '#'
            globalOcc += 1
            changed = True
        else:
            lm += 'L'
    elif seats[m-1][n-1] == '#':
        lm += '#'
        globalOcc += 1

    newSeats.append(lm)

    seats = newSeats
print(globalOcc)
