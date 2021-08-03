n = int(input())
count = 0

count += n // 5
n = n%5
count += n//4
n = n%4
count += n//3
n = n%3
count += n//2
n = n%2
count += n//1
n = n%2
print(count)
    