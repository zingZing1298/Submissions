test = int(input())
x = 0
for cases in range(test):
    a,b,k = map(int,input().split())
    if(k%2 == 0):
        x = (k//2)*a - (k//2)*b
    else:
        x = (k//2 + 1)*a - (k//2)*b
    print(x)