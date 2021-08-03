n = int(input())
name = input()
count = 0

for i in range(n):
    if(i+2 <= n-1):
        if(name[i]== 'x'and name[i+1]=='x' and name[i+2]=='x'):
            count += 1

print(count)
