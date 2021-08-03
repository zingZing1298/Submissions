#Objective of the code is to check for solution of Power game
def merge(arr,n,lo,hi):
    mid = (li + ho)//2
    p1,p2 = 0,mid+1
    temp = []
    while(p1<= mid and p2<= hi):
        if(arr[p1]<arr[p2]):
            temp.append(arr[p1])
            p1+= 1
        else:
            temp.append(arr[p2])
            p2+= 1
    while(p1<=mid):
        temp.append(arr[p1])
        p1 += 1
    while(p2<=hi):
        temp.append(arr[p2])
        p2 += 1
    for i in range(lo,hi+1):
        arr[i] = temp[i-lo]
    return arr

def mergeSort(arr,n,lo,hi):
    if(lo == hi):
        return
    mid = (lo+hi)//2
    mergeSort(arr,n,lo,mid)
    mergeSort(arr,n,mid+1,hi)
    return merge(arr,n,lo,hi)

def powerGame(teama,teamb,n):
    p1,p2 = 0,0
    count = 0
    while(p1<n and p2<n):
        if(p1 == n-1):
            return count
        
        if(teama[p1] > teamb[p2]):
            count += 1
            p1 += 1
            p2 += 1
        
        else:
            p1+= 1
    return count
         
if __name__ == "__main__":
    test = int(input())
    for cases in range(test):
        n = int(input())
        teama = list(map(int,input().split()))
        teama = mergesort(arr,n,0,n-1)
        teamb = list(map(int,input().split()))
        teamb = mergesort(arr,n,0,n-1)
        print(powerGame(teama,teamb,n))