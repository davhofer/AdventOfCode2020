f = open('test18.txt')

sum = 0

def nextSrc(i,line):
    ints = ['0','1','2','3','4','5','6','7','8','9']
    if line[i] == ' ':
        i += 1
    if line[i] in ints:
        return int(line[i]),i
    if line[i] == '(':
        return evalExpression(i+1,line)


def nextOp(i,line):
    open = 0
    while i < len(line)-1:
        if line[i] == '*':
            return '*'
        if line[i] == '+':
            return '+'
        if line[i] == '(':
            open += 1
            while open > 0:
                i += 1
                if line[i] == '(':
                    open += 1
                if line[i] == ')':
                    open -= 1
        i += 1
    return None




def evalExpression(i,line):
    print('eval from ' + str(i))
    ints = ['0','1','2','3','4','5','6','7','8','9']
    n = len(line)-1
    state = 0


    while i < n:

        #print('read ' + str(line[i]))
        if line[i] == ' ':
            i+=1
            continue
        if line[i] in ints:
            if state == 0:
                state = 1
                src1 = int(line[i])
            elif state == 2:
                state = 3
                src2 = int(line[i])
            i+=1
        if line[i] == '(':
            #print('new eval')
            if state == 0:
                state = 1
                src1,i = evalExpression(i+1,line)
            elif state == 2:
                state = 3
                src2,i = evalExpression(i+1,line)
        if state == 3 and op == '*':
            print("operation is *, check for next op")
            print('i = ' + str(i))
            while nextOp(i,line) != None and nextOp(i,line) == '+':

                if nextSrc(i+2,line) == None:
                    break
                #print("nxtsrc")
                #print(nextSrc(i+2,line))


                nxt,i = nextSrc(i+2,line)

                src2 = src2 + nxt
                #print(src2)
                i += 1

        if i<n and line[i] == '+':
            if state == 1:
                state=2
            op = '+'
            i += 1
        if i<n and line[i] == '*':
            if state == 1:
                state=2
            op = '*'
            i += 1

        if state == 3:
            print('doing calc')
            if op == '+':
                src1 = src1 + src2
            elif op == '*':
                src1 = src1 * src2
            state = 1
        #print('res = ' + str(src1))
        #print('i = ' + str(i))
        if i<n and line[i] == ')':
            #print('end eval')
            i += 1
            return src1,i




    return src1,i

print(evalExpression(0,'6 + 7 * (3 * 2 + (3 * 8 + 9) * (4 + 2 + 5 + 7) + 8) + 7 + 5 * (6 * (7 + 6 + 5) + 3 + 4 * (8 + 4 + 9 + 3))'))

for l in f.readlines():
    print(evalExpression(0,l))
    sum += evalExpression(0,l)[0]

print(sum)
