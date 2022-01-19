str1 = list(input())
s1 = 0
s = str(['0123456789'])
flag = False
for i in str1:
    if s in str1:
        flag = True
        break
if flag == True:
    print('Цифра')
else:
    print(str1)