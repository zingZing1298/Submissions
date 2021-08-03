def hasSumPair(arr,n,k):
    lo,hi = 0,n-1
    flag = 0
    while(lo<hi):
        s = arr[lo]+arr[hi]
        if(s == k):
            flag = 1
        elif(s<k):
            lo += 1
        elif(s>k):
            hi -= 1
        else:
            flag = 0
    if(flag == 1):
        return True
    else:
        return False
if __name__ == "__main__":
    test = int(input())
    for cases in range(test):
        n,k = map(int,input().split())
        arr = list(map(int,input().split()))
        arr.sort()
        print(hasSumPair(arr,n,k))
