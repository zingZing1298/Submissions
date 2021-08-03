n =int(input())
count = 0
while(n>0):
    count += n // 100
    n = n % 100
    count += n // 20
    n = n % 20
    count += n // 10
    n = n % 10
    count += n // 5
    n = n % 5
    count += n//1
    n = n % 1
print(count)