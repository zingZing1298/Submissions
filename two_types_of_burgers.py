test = int(input())

for cases in range(test):
    b,p,f = map(int,input().split())
    h,c = map(int,input().split())
    ans = 0

    if(h > c):
        ans += h * min(b //2 ,p)
        b -= 2 * min(b //2 ,p)
        ans += c * min(b //2 ,f)
        c -= 2 * min(b//2, f)
    else:
        ans += c * min(b//2,f)
        b -= 2 * min(b //2 ,f)
        ans += h * min(b //2 ,p)
        b -= 2 * min(b//2, p)

    print(ans)
        
