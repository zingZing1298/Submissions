def firstMissingInteger(arr,n):
    arr.sort()
    i = 0
    pos = 0
    while(i<n and arr[i]<=0):
        i = i+1
    pos = i
    if(max(arr)<=0):
        return 1
    elif(arr[pos]!=1):
        return 1
    elif(max(ar)>0):
        for i in range(n-1):
            if(arr[i] != arr[i+1] - 1):
                return ar[i]+1
        return arr[n-1] + 1



if __name__ == "__main__":
    test = int(input())
    for cases in range(test):
        arr = list(map(int,input().split()))
        n= len(arr)
        print(firstMissingInteger(arr,n))