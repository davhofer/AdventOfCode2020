f = open("input6.txt","r")

letters_orig = [0]*26

sum = 0

letters = letters_orig.copy()
people = 0
for l in f.readlines():
    if len(l) != 1:
        people += 1
        for i in range(len(l[:-1])):
            letters[ord(l[i])-97] += 1
        #newline, endgroup
    else:
        for i in range(26):
            if letters[i] == people:
                sum += 1
        letters = letters_orig.copy()
        people = 0
for i in range(26):
    if letters[i] == people:
        sum += 1

print(sum)
