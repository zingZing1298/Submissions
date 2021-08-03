n = int(input())
arr = list(map(int,input().split()))
flag = 0
for i in range(n):
    if(arr[i]== 1):
        flag = 1
        break
    else:
        flag = 0
if(flag == 1):
    print('Hard')
else:
    print('Easy')