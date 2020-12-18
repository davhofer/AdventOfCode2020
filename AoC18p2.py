f = open('input18.txt')

debug = False
sum = 0
def evalExpression(i,line):
    if debug:
        print("eval expression")
    ints = ['0','1','2','3','4','5','6','7','8','9']
    n = len(line)-1
    state = 0
    terms = []
    while i < n:
        token = line[i]
        if token == ' ':
            i += 1
            continue
        if debug:
            print('reading : ' + token)
        if token in ints:
            if state == 0:
                state = 1
                src1 = int(line[i])
            elif state == 2:
                state = 3
                src2 = int(line[i])
            i+=1
        elif token == '(':
            #print('new eval')
            i += 1
            if state == 0:
                state = 1
                src1,i = evalExpression(i,line)
            elif state == 2:
                state = 3
                src2,i = evalExpression(i,line)

        elif token == '+':

            state=2
            op = '+'
            i += 1
        elif token == '*':
            terms.append(src1)
            i+=1
            state = 0
            continue
        elif token == ')':
            i += 1
            for x in terms:
                src1 *= x
            if debug:
                print('src1 = ' + str(src1))

            return src1,i

        if state==3:
            if op == '+':
                src1 = src1 + src2

    for x in terms:
        src1 *= x
    if debug:
        print('src1 = ' + str(src1))
    return src1,i

#print(evalExpression(0,'1 + (2 * 3) + (4 * (5 + 6))'))
#print(evalExpression(0,'6 + 7 * (3 * 2 + (3 * 8 + 9) * (4 + 2 + 5 + 7) + 8) + 7 + 5 * (6 * (7 + 6 + 5) + 3 + 4 * (8 + 4 + 9 + 3))'))
for l in f.readlines():
    ev = evalExpression(0,l)
    print(ev)
    sum += ev[0]

print(sum)
