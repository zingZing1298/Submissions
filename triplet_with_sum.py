def returnsAnswer(arr,n,k):
    flag = 0
    for i in range(n-2):
        add = k - arr[i]
        #print("a:",arr[i],"b+c:",add)
        p1,p2 = i+1,n-1
        while(p1<p2):
            if(arr[p1]+arr[p2]==add and p1<p2):
                flag = 1
                break
            elif(arr[p1]+arr[p2]>add and p2>i+1):
                p2= p2 - 1
                #print('p2:',p2,"ans:",arr[p1]+arr[p2])
            elif(arr[p1]+arr[p2]<add and p1<n-1):
                p1=p1 + 1
                #print('p1:',p1,"ans:",arr[p1]+arr[p2])
            
    if(flag == 1):
        return "true"
    else:
        return "false"
    
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
    
if __name__ == '__main__':
    test = int(input())
    for cases in range(test):
        n,k = map(int,input().split())
        arr = list(map(int,input().split()))
        arr = mergeSort(arr,n,0,n-1)
        #print(arr)
        print(returnsAnswer(arr,n,k))