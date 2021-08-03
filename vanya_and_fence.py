p,f = map(int,input().split())
arr = list(map(int,input().split()))
count = 0
for i in range(p):
    if(arr[i]<=f):
        count += 1
    else:
        count += 2

print(count)