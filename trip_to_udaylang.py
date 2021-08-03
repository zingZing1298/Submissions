n = int(input())
new = []
flag = 0

for i in range(n):
    r = list(map(str, input().split('|')))
    new.append(r)

for i in range(len(new)):
    for j in range(len(new[0])):
        if new[i][j] == 'OO':
            new[i][j] = "++"
            flag = 1
            break
    if flag == 1:
        break
    else:
        continue
    
if(flag == 1):
    print('YES')
    for i in range(len(new)):
        print("|".join(new[i]))
else:
    print("NO")
    
