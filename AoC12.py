f = open('input12.txt','r')
pos = [0,0]
dir = [1,0]
def dir_change(cdir, change):
    if change[1:3] == '18':
        return [-cdir[0],-cdir[1]]
    elif change == 'R90' or change == 'L27':
        return [cdir[1],-cdir[0]]
    elif change == 'L90' or change == 'R27':
        return [-cdir[1],cdir[0]]
for l in f.readlines():
    if l[0] == 'N':
        pos[1] += int(l[1:-1])
    elif l[0] == 'S':
        pos[1] -= int(l[1:-1])
    elif l[0] == 'E':
        pos[0] += int(l[1:-1])
    elif l[0] == 'W':
        pos[0] -= int(l[1:-1])
    elif l[0] == 'F':
        pos[0] += int(l[1:-1])*dir[0]
        pos[1] += int(l[1:-1])*dir[1]
    elif l[0] == 'R' or l[0] == 'L':
        dir = dir_change(dir,l[:3])
print("part 1 sol = " + str(abs(pos[0]) + abs(pos[1])))
f.close()

# PART 2
f = open('input12.txt','r')
def dir_change_wp(cdir, change):
    if change[1:3] == '18':
        return [-cdir[0],-cdir[1]]
    elif change == 'R90' or change == 'L27':
        return [cdir[1],-cdir[0]]
    elif change == 'L90' or change == 'R27':
        return [-cdir[1],cdir[0]]
ship = [0,0]
wp = [10,1]
for l in f.readlines():
    if l[0] == 'N':
        wp[1] += int(l[1:-1])
    elif l[0] == 'S':
        wp[1] -= int(l[1:-1])
    elif l[0] == 'E':
        wp[0] += int(l[1:-1])
    elif l[0] == 'W':
        wp[0] -= int(l[1:-1])
    elif l[0] == 'F':
        ship[0] += int(l[1:-1])*wp[0]
        ship[1] += int(l[1:-1])*wp[1]
    elif l[0] == 'R' or l[0] == 'L':
        wp = dir_change_wp(wp,l[:3])
print("part 2 sol = " + str(abs(ship[0]) + abs(ship[1])))
