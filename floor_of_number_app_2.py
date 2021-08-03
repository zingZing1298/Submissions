# Objective of the program or code is to find floor of number using the approach that queries need to be saved into an array, using two pointers and mergeSort
import copy

def merge(arr,n,lo,hi):
    mid = (lo + hi) // 2
    p1 = lo
    p2 = mid
    temp = []
    while(p1<=mid and p2<= hi):
        if(arr[p1]<arr[p2]):
            temp.append(arr[p1])
            p1 += 1
        else:
            temp.append(arr[p2])
            p2 += 1
    while(p1<=mid):
        temp.append(arr[p1])
        p1 += 1
    while(p2<=hi):
        temp.append(arr[p2])
        p2 += 1
    for i in range(lo,hi+1):
        arr[i] = temp[i - lo]
    return arr

def mergeSort(arr,n,lo,hi):
    if(lo == hi):
        return
    mid = (lo + hi)//2
    mergeSort(arr,n,lo,mid)
    mergeSort(arr,n,mid+1,hi)
    return merge(arr,n,lo,hi)

def twoPointerSol(arr,q,n,sizeq,ans):
    p1,p2 = 0,0 #p1 points on arr and p2 points on query,these pointers help us find the answer
    while(p1<n and p2<sizeq):


            
    
    
    
    
    
    
    
    
    
    
    while(p1<n and p2<sizeq and arr[p1]<= q[p2]):
        ans[p2] = arr[p1]
        p2 += 1
        p1 += 1


if __name__ == "__main__": 
    n = in(input())
    arr = list(map(int,input().split()))
    size_query = int(input().split())
    original_query = int(input())
    for i in range(size_query):
        original_query.append(int(input()))

    arr = mergeSort(arr,n,0,n-1)
    query = copy.copy(original_query)
    query = mergeSort(query,size_query,0,size_query-1)
    ans = [-2**31 for i in range(size_query)]
    twoPointerSol(arr,query,n,size_query,ans)