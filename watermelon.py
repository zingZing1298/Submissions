weight = int(input())
flag = 0
for i in range(0,weight,2):
    for j in range(i,weight,2):
        if i+j == weight:

            flag = 1

if(flag == 1):
    print('YES')
elif(flag == 0):
    print('NO')