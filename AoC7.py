f = open('input8.txt','r')

lines = []
for l in f.readlines():
    l1 = l[:-1]
    lines.append(l1.split(" "))
n = len(lines)
exec = [0]*len(lines)
f.close()
for i in range(n):
    f = open('input8.txt','r')
    lines = []
    for l in f.readlines():
        l1 = l[:-1]
        lines.append(l1.split(" "))
    n = len(lines)
    exec = [0]*len(lines)

    def runcode(EXEC,LINES,i):
        print(i)
        if LINES[i][0] == 'nop':
            LINES[i][0] = 'jmp'
        elif LINES[i][0] == 'jmp':
            LINES[i][0] = 'nop'
        else:
            print('nah')
            return
        print(lines[i])
        acc = 0
        PC = 0
        while EXEC[PC]==0:
            if LINES[PC][0] == 'acc':
                acc += int(LINES[PC][1])
                EXEC[PC] = 1
                PC += 1
            elif LINES[PC][0] == 'jmp':
                EXEC[PC] = 1
                PC += int(LINES[PC][1])
            elif LINES[PC][0] == 'nop':
                EXEC[PC] = 1
                PC += 1
            elif LINES[PC][0] == 'done':
                print('done')
                print(acc)
                print(i)
                print('-----------------------------')
                break




    runcode(exec,lines,i)
    f.close()
