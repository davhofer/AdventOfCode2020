f = open('input9.txt','r')

numbers = []
for l in f.readlines():
    numbers.append(int(l[:-1]))
#
# for i in range(25,len(numbers)):
#     good = False
#     for k in range(i-25,i):
#         if good:
#             break
#         for l in range(k,i):
#             if numbers[k] + numbers[l] == numbers[i]:
#                 good = True
#                 break
#     if not good:
#         print(numbers[i])
#         break

#
# print(numbers[548] + numbers[564])
# s = 0
# for i in range(548,565):
#     print(numbers[i])
#     s += numbers[i]
#
# print("--------------------sum-------------")
# print(s)
# 137282719
# 72411414
#
n = 1721308972
# print("------------n-------------------")
# print(n)




for i in range(len(numbers)):
    for j in range(i,len(numbers)):
        sum = 0
        for k in range(i,j):
            sum += numbers[k]
        if sum == n:
            print(str(i) + ", " + str(j-1))
            break
