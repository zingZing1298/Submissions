n= int(input())
arr = list(map(int,input().split()))
new = []

for i in range(1,n+1):
    for j in range(0,n):
        if(i == arr[j]):
            new.append(j+1)
print(*new)