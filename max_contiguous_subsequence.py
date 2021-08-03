def maxContiguousSubsequence(arr,n):
    arr.sort()
    start = 0
    ans,count = 1,1
    while(start<n):
        if(start+1<n and arr[start] == arr[start+1]):
            start += 1
        elif( start+1 < n and abs((arr[start+1]) - (arr[start])) == 1 ):
            count+=1
            start+=1
            ans = max(ans,count)
        else:
            count = 1
            start += 1   
    return ans
if __name__ == "__main__":
    test = int(input())
    for cases in range(test):
        n = int(input())
        arr = list(map(int,input().split()))
        print(maxContiguousSubsequence(arr,n))s