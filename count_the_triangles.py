def countTriangles(arr,n):
    count = 0
    for i in range(n-1,0,-1):
        p1,p2 = 0,i-1
        while(p1<p2):
            if(arr[p1]+arr[p2]>arr[i]):
                count += p2 - p1
                p2 -=1 
            else:
                p1+=1
    return count

def merge(arr,n,lo,hi):
    mid = (lo+hi)//2
    p1,p2 = lo,mid+1
    temp = []
    while(p1<=mid and p2<=hi):
        if(arr[p1]<arr[p2]):
            temp.append(arr[p1])
            p1 += 1
        else:
            temp.append(arr[p2])
            p2+= 1
    while(p1<=mid):
        temp.append(arr[p1])
        p1 += 1
    while(p2<= hi):
        temp.append(arr[p2])
        p2 += 1
    for i in range(lo,hi+1):
        arr[i] = temp[i-lo]
    return arr

def mergeSort(arr,n,lo,hi):
    if(lo == hi):
        return
    mid =(lo+hi)//2
    mergeSort(arr,n,lo,mid)
    mergeSort(arr,n,mid+1,hi)
    return merge(arr,n,lo,hi)


if __name__ == "__main__":
    test = int(input())
    for cases in range(test):
        n = int(input())
        arr = list(map(int,input().split()))
        arr = mergeSort(arr,n,0,n-1)
        print(countTriangles(arr,n))