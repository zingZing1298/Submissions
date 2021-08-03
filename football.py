n =int(input())
count = 0
flag = 0

for i in range(n):
    if(n[i+1]-n[i] == 0):
        flag = 1
        count += 1
    else:
        flag = 0

if(flag == 1 and count >= 7):
    print('YES')
else:
    print('NO')