# Objective is to find pair of elements who difference between two elements
def pairdiff(ar,n,k):
    flag=0
    for i in range(n):
        b=ar[i]
        #print('a:',a) 
        a=b+k
        #print('b:',b)
        if(BSR(ar,a,i+1,n-1)==True):
            flag=1
            break
        else:
            flag=0
    if(flag==1):
        return 'true'
    else:
        return 'false'

def BSR(ar,b,l,h):
    while(l<=h):
        m=(l+h)//2
        #print(ar[m],b)
        if(b<ar[m]):
            h=m-1
        elif(b>ar[m]):
            l=m+1
        else:
            #print(ar[m],b)
            return True
    return False


if __name__=='__main__':
    t=int(input())
    for case in range(t):
        n,k=map(int,input().split())
        ar=list(map(int,input().split()))
        ar.sort()
        #print(ar)
        print(pairdiff(ar,n,k))
