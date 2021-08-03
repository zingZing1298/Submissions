n = int(input())

last = '00'
count = 0

for i in range(n):
    a = input()
    if a != last:
        count += 1
    last = a
print(count)