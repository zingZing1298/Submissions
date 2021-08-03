try:
    test = int(input())
    for cases in range(test):
        n,m = map(int,input().split())
        fruits = list(map(int,input().split()))
        price = list(map(int,input().split()))
        h = [0 for i in range(m+1)]

        for i in range(1,m+1):
            for j in range(n):
                if(i == fruits[j]):
                    h[i] += price[j]

        j = 0    
        for i in range(1,m+1):
            if (i not in fruits):
                h.pop(i-j)
                j+= 1
    
        h.pop(0)
        print(min(h))

except:
    pass