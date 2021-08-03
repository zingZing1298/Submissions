n = int(input())
s = input()
cs = 0
cf = 0
for i in range(0,n):
    if(i+1<n):
        if(s[i] == 'S' and s[i+1] == 'F'):
            cf += 1
        elif(s[i] == 'F' and s[i+1] == 'S'):
            cs += 1

if(cf > cs):
    print('YES')
else:
    print('NO')
