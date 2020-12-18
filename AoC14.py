#b = BitArray(bin='11111111')
#b.uint

f = open('test14.txt','r')



def applyBitmask(x, bitmsk):
    res = ''
    for i in range(36):
        if bitmsk[i] == 'X':
            res += x[i]
        else:
            res += bitmsk[i]
    return res

def bin(x):
    return "{0:b}".format(x)


def applyBitmask2(x,bitmsk):
    addr_base = ''
    nx = 0
    for i in range(36):
        if bitmsk[i] == '0':
            addr_base += x[i]
        elif bitmsk[i] == '1':
            addr_base += '1'
        elif bitmsk[i] == 'X':
            addr_base += 'X'
            nx += 1
    #print(addr_base)
    res = []
    for i in range(2**nx):
        comb = bin(i)

        #print(comb)
        comb = '0'*(nx-len(comb))+comb
        print(comb)
        #print(comb)
        addr = ''
        xcount = 0
        for j in range(36):
            if addr_base[j] == 'X':
                addr += comb[xcount]
                xcount += 1
            else:
                addr += addr_base[j]
        #print(addr)
        res.append(addr)
        #print(res)
    return res



def dez(x):
    return int(x, 2)

mem = {}
mask = ""
for l in f.readlines():
    if l[:3] == 'mas':
        mask = l.split(' ')[2][:-1]
    elif l[:3] == 'mem':
        addr = l.split(']')[0][4:]

        x = l.split(' ')[2][:-1]

        #b = '0'*(36-len(bin(int(x))))+bin(int(x))
        b2 = '0'*(36-len(bin(int(addr))))+bin(int(addr))
        for a in applyBitmask2(b2,mask):
            mem[dez(a)] = int(x)#applyBitmask(b,mask)



sum = 0
for k in mem.keys():
    sum += mem[k]

print(sum)
