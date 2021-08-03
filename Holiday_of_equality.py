n = int(input())

arr = list(map(int,input().split()))
count = 0
max1 = max(arr)
#print(max1)

for i in range(n):
    count = count + (max1-arr[i])
print(count)
