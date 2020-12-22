import itertools
import math
import re
f = open('day20.txt','r')
#
# tiles = {}
# adj = {}
# l = f.readline()[:-1]
# l = l[:-1]
# while len(l) > 3:
#     if "Tile" in l:
#         borders = []
#         b_right = ''
#         b_left = ''
#         id = l.split(' ')[1][:-1]
#         for i in range(10):
#             l = f.readline()[:-1]
#             if i == 0:
#                 borders.append(l)
#             b_right = b_right + l[-1]
#             b_left = l[0] + b_left
#             if i == 9:
#                 borders.append(l[::-1])
#         borders.append(b_left)
#         borders.append(b_right)
#         tiles[id] = borders
#         print(borders)
#         l = f.readline()
#         l = f.readline()[:-1]
# keys = tiles.keys()
# ans = 1
# for i in tiles.keys():
#     count = 0
#     for j in tiles.keys():
#         if i == j:
#             continue
#         combs = itertools.product(tiles[i],tiles[j])
#         for c in combs:
#             if c[0] == c[1] or c[0] == c[1][::-1]:
#                 count += 1
#     adj[i] = count
#     if count == 2:
#         ans *= int(i)
# print(ans)

def printtile(tile):
    for i in range(len(tile)):
        print(tile[i])

def flip_tile(tile):
    n = len(tile)
    n_tile = []
    for i in range(n):
        l = ''
        for j in range(n):
            l += tile[j][i]
        n_tile.append(l)
    return n_tile


def flip_borders(borders):
    n_borders = {}
    top = borders['top']
    n_borders['top'] = borders['left'][::-1]
    n_borders['left'] = top[::-1]
    bot = borders['bot']
    n_borders['bot'] = borders['right'][::-1]
    n_borders['right'] = bot[::-1]
    return n_borders


def rotate_borders(borders,times):
    if times == 1:
        n_borders = {}
        top = borders['top']
        n_borders['top'] = borders['left']
        n_borders['left'] = borders['bot']
        n_borders['bot'] = borders['right']
        n_borders['right'] = top
        return n_borders
    if times > 1:
        return rotate_borders(rotate_borders(borders,times-1),1)

def rotate_tile(tile,times):
    m = len(tile)
    n = len(tile[0])
    n_tile = []

    if times == 2:
        for i in range(m):
            n_tile.append(tile[m-i-1][::-1])
        return n_tile
    elif times == 1:
        for i in range(n):
            l = ''
            for j in range(m):
                l += tile[j][i]
            l = l[::-1]
            n_tile.append(l)
        return n_tile
    elif times == 3:
        return rotate_tile(rotate_tile(tile,2),1)

test = ['123','456','789']
print(rotate_tile(test,1))
print(rotate_tile(test,2))
print(rotate_tile(test,3))

COUNT_HT = 0
borders = {}
tiles = {}
adj = {}
has_adj = {}
l = f.readline()[:-1]
l = l[:-1]
corners = []
walls = []
center = []
while len(l) > 3:
    if "Tile" in l:
        tile = []
        b = {}
        b_right = ''
        b_left = ''
        id = l.split(' ')[1][:-1]
        for i in range(10):
            l = f.readline()[:-1]
            for j in range(len(l)):
                if l[j] == '#':
                    COUNT_HT += 1
            tile.append(l)
            if i == 0:
                b['top'] = l
            b_right = b_right + l[-1]
            b_left = l[0] + b_left
            if i == 9:
                b['bot'] = l[::-1]
        b['left'] = b_left
        b['right'] = b_right
        borders[id] = b
        tiles[id] = tile
        l = f.readline()
        l = f.readline()[:-1]

#
# print('HASHTAGS: ' + str(COUNT_HT))
#
# print('-----------------------')
# printtile(tiles['1693'])
# print('-----------------------')
#
# print(borders['1693']['right'])
# print('-----------------------')
#
# print(borders['1693']['left'])
# print('-----------------------')
#
# print(borders['1693']['bot'])
# print('-----------------------')
# print('--------------------------------------------------')
#
# printtile(rotate_tile(tiles['1693'],3))
# print()
# print()
# print(rotate_borders(borders['1693'],3))
#
# print('--------------------------------------------------')
#
for i in tiles.keys():
    count = 0
    has_adj_i = {'top':False,'bot':False,'left':False,'right':False}
    #[top,bot,left,right]
    for j in tiles.keys():
        if i == j:
            continue
        combs = itertools.product(['top','bot','left','right'],['top','bot','left','right'])
        #combs = itertools.product(tiles[i],tiles[j])
        for c in combs:
            if borders[i][c[0]] == borders[j][c[1]][::-1] or borders[i][c[0]] == borders[j][c[1]]:
                count += 1
                has_adj_i[c[0]] = True
    if count == 2:
        corners.append(i)
    elif count == 3:
        walls.append(i)
    elif count == 4:
        center.append(i)
    else:
        print('invalid count: ' + str(count))
    has_adj[i] = has_adj_i
for id in has_adj.keys():
    for k in has_adj[id].keys():
        if not has_adj[id][k]:
            borders[id][k] = ''

    adj[i] = count
#print(len(tiles.keys()))
n = int(math.sqrt(len(tiles.keys())))
#print(n)
full = []
for i in range(n):
    full.append([0]*n)

#print(' corners ---------------------------------')
#print(corners)
for i in range(n):
    for j in range(n):
        if i==0 and j==0:
            id_c = corners[0]
            full[i][j] = id_c
            if has_adj[id_c]['top'] and has_adj[id_c]['right']:
                tiles[id_c] = rotate_tile(tiles[id_c],1)
                borders[id_c] = rotate_borders(borders[id_c],1)
            elif has_adj[id_c]['bot'] and has_adj[id_c]['left']:
                tiles[id_c] = rotate_tile(tiles[id_c],3)
                borders[id_c] = rotate_borders(borders[id_c],3)
            elif has_adj[id_c]['left'] and has_adj[id_c]['top']:
                tiles[id_c] = rotate_tile(tiles[id_c],2)
                borders[id_c] = rotate_borders(borders[id_c],2)

        elif j > 0:
            found = False
            for id in tiles.keys():
                if not found:
                    for bk in borders[id].keys():
                        if id != full[i][j-1] and borders[id][bk] == borders[full[i][j-1]]['right'][::-1]:
                            #match found
                            found = True
                            full[i][j] = id

                            if bk == 'top':
                                tiles[id] = rotate_tile(tiles[id],3)
                                borders[id] = rotate_borders(borders[id],3)
                            elif bk == 'right':
                                tiles[id] = rotate_tile(tiles[id],2)
                                borders[id] = rotate_borders(borders[id],2)
                            elif bk == 'bot':
                                tiles[id] = rotate_tile(tiles[id],1)
                                borders[id] = rotate_borders(borders[id],1)
                            break
                        elif id != full[i][j-1] and flip_borders(borders[id])[bk] == borders[full[i][j-1]]['right'][::-1]:
                            borders[id] = flip_borders(borders[id])
                            found = True
                            full[i][j] = id
                            tiles[id] = flip_tile(tiles[id])
                            if bk == 'top':
                                tiles[id] = rotate_tile(tiles[id],3)
                                borders[id] = rotate_borders(borders[id],3)
                            elif bk == 'right':
                                tiles[id] = rotate_tile(tiles[id],2)
                                borders[id] = rotate_borders(borders[id],2)
                            elif bk == 'bot':
                                tiles[id] = rotate_tile(tiles[id],1)
                                borders[id] = rotate_borders(borders[id],1)
                            break

        elif j == 0 and i > 0:
            found = False
            for id in tiles.keys():
                if not found:
                    for bk in borders[id].keys():
                        if id != full[i-1][0] and borders[id][bk] == borders[full[i-1][0]]['bot'][::-1]:
                            found = True
                            full[i][j] = id
                            if bk == 'left':
                                tiles[id] = rotate_tile(tiles[id],1)
                                borders[id] = rotate_borders(borders[id],1)
                            elif bk == 'bot':
                                tiles[id] = rotate_tile(tiles[id],2)
                                borders[id] = rotate_borders(borders[id],2)
                            elif bk == 'right':
                                tiles[id] = rotate_tile(tiles[id],3)
                                borders[id] = rotate_borders(borders[id],3)
                            break
                        elif id != full[i-1][0] and flip_borders(borders[id])[bk] == borders[full[i-1][0]]['bot'][::-1]:
                            found = True
                            full[i][j] = id
                            borders[id] = flip_borders(borders[id])
                            tiles[id] = flip_tile(tiles[id])
                            if bk == 'left':
                                tiles[id] = rotate_tile(tiles[id],1)
                                borders[id] = rotate_borders(borders[id],1)
                            elif bk == 'bot':
                                tiles[id] = rotate_tile(tiles[id],2)
                                borders[id] = rotate_borders(borders[id],2)
                            elif bk == 'right':
                                tiles[id] = rotate_tile(tiles[id],3)
                                borders[id] = rotate_borders(borders[id],3)
                            break

#print(full)
#
# for i in full[0]:
#     print(tiles[i])
#
# printtile(tiles['1693'])
# # print(borders['1693']['right'])
# # print(borders['1693']['left'])
# print()
#
# print()
# printtile(tiles['1783'])

n_tiles = len(full)
n = len(tiles['1693'])
#n = len(tiles['3079'])
print(n_tiles)
print(n)
full_tile = []
for blockline in range(n_tiles):
    for line in range(n-2):
        l = ''
        for block in range(n_tiles):
            l+=tiles[full[blockline][block]][line+1][1:-1]
        full_tile.append(l)
#
# for l in full_tile:
#     print(l)
#
# print()
# print()
#
# for l in rotate_tile(full_tile,1):
#     print(l)
#
#
# print(str(len(full_tile))+", "+str(len(full_tile[0])))
# print(str(len(rotate_tile(full_tile,1)))+", "+str(len(rotate_tile(full_tile,1)[0])))

pattern_m = "#....##....##....###"
monsters = 0
#on top: at pos start+18 must be #
#on bottom: at pos start+1 and start+4 and start+7 and start+10 and start+13 and start+16 must be #
for r in range(4):
    for i in range(1,len(full_tile)-1):
        pos = 0
        match = re.search(pattern_m,full_tile[i])
        while(match != None):

            start = match.start()+pos
            if full_tile[i-1][start+18] == '#' and full_tile[i+1][start+1] == '#' and full_tile[i+1][start+4] == '#' and full_tile[i+1][start+7] == '#' and full_tile[i+1][start+10] == '#' and full_tile[i+1][start+13] == '#' and full_tile[i+1][start+16] == '#':
                print("gotcha")
                print("Rotation: " + str(r))

                monsters += 1
                pos += 20
            if pos>len(full_tile[i]):
                break
            match = re.search(pattern_m,full_tile[i][pos+start+1:])
            pos = pos + start+1
    full_tile = rotate_tile(full_tile,1)

full_tile = flip_tile(full_tile)
for r in range(4):
    for i in range(1,len(full_tile)-1):
        pos = 0
        match = re.search(pattern_m,full_tile[i])
        while(match != None):


            start = match.start()+pos
            if full_tile[i-1][start+18] == '#' and full_tile[i+1][start+1] == '#' and full_tile[i+1][start+4] == '#' and full_tile[i+1][start+7] == '#' and full_tile[i+1][start+10] == '#' and full_tile[i+1][start+13] == '#' and full_tile[i+1][start+16] == '#':
                print("gotcha")
                print("Rotation: " + str(r))
                monsters += 1

                #
                # l = full_tile[i-1]
                # full_tile[i-1] = l[0:18]+'O'+l[19:]
                # l = full_tile[i]
                # # "#....##....##....###"
                # full_tile[i] = l[0:start]+'O'+l[start+1:start+5]+'OO'+l[start+7:start+11]+'OO'+l[start+13:start+17]+'OOO'+l[start+20:]
                # l = full_tile[i+1]
                # full_tile[i+1] = l[0:start+1]+'O'+l[start+2:start+4]+'O'+l[start+5:start+7]+'O'+l[start+8:start+10]+'O'+l[start+11:start+13]+'O'+l[start+12:start+16]+'O'+l[start+17:]
            # if pos>len(full_tile[i]):
            #     break
            match = re.search(pattern_m,full_tile[i][pos+start+1:])
            pos = pos + start+1
    full_tile = rotate_tile(full_tile,1)


cnt = 0
for i in range(len(full_tile)):
    for j in range(len(full_tile[i])):
        if full_tile[i][j] == '#':
            cnt += 1
HASHTAGS = cnt
print(monsters)
print(HASHTAGS)
print(monsters*15)
print(HASHTAGS-monsters*15)


                # full[i][j-1]
