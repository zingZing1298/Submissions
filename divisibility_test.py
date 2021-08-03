test = int(input())
for cases in range(test):
    a,b = map(int,input().split())
    if(b > a):
        print(b-a)
    elif(a%b == 0):
        print(0)
    else:
        rem = a%b
        print(b-rem)