# The objective is to find floor of any given query i.e X= max(arr[i]) <=x, Find X.
# Multiple approaches.Use BS AND merge Sort

def merge(arr,n,lo,hi): #Function to merge left and right subarrays from mergeSort
    mid = (lo + hi)//2
    temp = []
    p1,p2 = lo,mid+1
    while(p1 <= mid and p2 <= hi):
        if(arr[p1] < arr[p2]):
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
        arr[i] = temp[i - lo]
    return arr


def mergeSort(arr,n,lo,hi): #merge sort
    if(lo == hi):
        return
    mid =(lo+hi)//2
    mergeSort(arr,n,lo,mid)
    mergeSort(arr,n,mid+1,hi)
    return merge(arr,n,lo,hi)



def binarySearch(arr,n,key): #Function to find the floor using Binary Search
    
    print(arr)
    lo = 0
    hi = n-1
    ans = -2**31
    while(lo<=hi):
        mid = (lo+hi)//2
        if(arr[mid]<=key):
            ans = arr[mid]
            lo = mid + 1
        else:
            hi = mid - 1
    print(ans)

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int,input().split()))
    arr = mergeSort(arr,n,0,n-1)
    print(arr)
    query = int(input())
    for queries in range(query):
        x = int(input())
        binarySearch(arr,n,x)