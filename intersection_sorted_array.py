def solve(a,b):
    p1,p2 = 0,0
    new = []
    while(p1<len(a) and p2<len(b)):
        if(a[p1] < b[p2]):
            p1+= 1
        elif(a[p1] > b[p2]):
            p2+=1
        else: 
            new.append(a[p1])
            p1+=1
            p2+=1
    return new

if __name__ == "__main__":
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    print(solve(a,b))