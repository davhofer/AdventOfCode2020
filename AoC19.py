import itertools
f = open('input19.txt','r')
rules = {}
msgs = []
maxlen = 0
for l in f.readlines():
    line = l[:-1]
    if ':' in l:
        line = line.replace('"','')
        rules[line.split(': ')[0]] = (line.split(': ')[1]).split(' | ')
    else:
        if len(line) > maxlen:
            maxlen = len(line)
        msgs.append(line)


rules['8'] =  ['42','42 8']
rules['11'] = ['42 31','42 11 31']
print(rules)
print('max:' + str(maxlen))

def buildrule(num,rules,depth,maxlen):
    print(depth)
    if depth > maxlen+2:
        return []
    if rules[num] == ['a'] or rules[num] == ['b']:
        return rules[num]
    ans = []
    for x in rules[num]:

        # go over all rules
        if len(x.split(' ')) == 3:
            a = buildrule(x.split(' ')[0],rules,depth+2,maxlen)
            b = buildrule(x.split(' ')[1],rules,depth+2,maxlen)
            c = buildrule(x.split(' ')[2],rules,depth+2,maxlen)
            if a == [] or b == [] or c == []:
                continue
            cartProd = itertools.product(a,b,c)

            for el in cartProd:
                #print(el)
                concat = ''
                for w in el:
                    if w != None:
                        concat += w
                ans.append(concat)
        elif len(x.split(' ')) == 2:

            #if it consists of 2 subrules, get the cartesian product of the 2
            a = buildrule(x.split(' ')[0],rules,depth+2,maxlen)
            b = buildrule(x.split(' ')[1],rules,depth+2,maxlen)
            if a == [] or b == []:
                continue
            cartProd = itertools.product(a,b)

            for el in cartProd:
                #print(el)
                concat = ''
                for w in el:
                    if w != None:
                        concat += w
                ans.append(concat)
        elif len(x.split(' ')) == 1:
            a = buildrule(x.split(' ')[0],rules,depth+1,maxlen)
            if a == []:
                continue
            for w in a:
                ans.append(w)
        else:
            return []
            print('error: length of x')
    return ans

itpr = buildrule('0',rules,0,maxlen)
strs = list(set(itpr))
print(len(strs))
#
# for el in strs:
#     print(el)
correct_msgs = set(strs).intersection(set(msgs))
print(len(correct_msgs))
