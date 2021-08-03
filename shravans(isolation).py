def center(s,n,c):
   
    for i in range(26):
        if(count[i]>=c):
            count[i]-=c
    print(sum(count))


if name=="name":
    t=int(input())
    for case in range(t):
        n,q=map(int,input().split())
        s=input()
        for query in range(q):
            c=int(input())
            center(s,n,c)