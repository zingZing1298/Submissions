a = list(map(int,input().split()))
s = input()
s1 = [int(i) for i in s]
sum = 0

for i in range(len(s1)):
    sum += a[s1[i]-1] 

print(sum)
