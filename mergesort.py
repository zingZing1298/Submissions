def merge(arr,lo,mid,hi):
    temp= []
    p1 =lo
    p2 = mid+1
    while(p1<=mid and p2<= hi):
        if(arr[p1] < arr[p2]):
            temp.append(arr[p1])
            p1+=1
        else:
            temp.append(arr[p2])
            p2+=1
    while(p1<=mid):
        temp.append(arr[p1])
        p1+=1
    while(p2<=hi):
        temp.append(arr[p2])
        p2+=1
    for i in range(lo,hi+1):
        arr[i] = temp[i - lo]
    return arr


def mergeSort(arr,lo,hi):
    if(lo == hi):
        return
    mid = (lo+hi)//2
    mergeSort(arr,lo,mid)
    mergeSort(arr,mid+1,hi)
    return merge(arr,lo,mid,hi)
