f = open("input2.txt","r")

# 1-3 a: abcde
# 1-3 b: cdefg
# 2-9 c: ccccccccc

valid = 0
for l in f.readlines():
    arr = l.split(" ")
    min = int(arr[0].split("-")[0])
    max= int(arr[0].split("-")[1])

    letter = arr[1][0]

    if arr[2][min-1] == letter or arr[2][max-1] == letter:
        if not (arr[2][min-1] == letter and arr[2][max-1] == letter):
            valid += 1


print(valid)
