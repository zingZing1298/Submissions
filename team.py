n = int(input())
new = []
count = 0
for i in range(n):
    r = list(map(int,input().split()))
    new.append(r)
for i in range(len(new)):
    if(sum(new[i]) >= 2):
        count += 1
print(count)