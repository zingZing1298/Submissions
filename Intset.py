try:
    test,k = map(int,input().split())
    count = 0
    for _ in range(test):
        n = int(input())
        if(n%k == 0):
            count += 1
    print(count)


except:
    pass