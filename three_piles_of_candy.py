test = int(input())

for cases in range(test):
    a,b,c = map(int, input().split())
    res = (a + b + c) // 2
    print(res)
    