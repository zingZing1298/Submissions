
def returnAns(arr,key):
    def binarySearch(arr,key,lo,hi):
        while(lo <= hi):
            mid = (hi +lo)//2
            if(arr[mid] == key):
                return True
            elif(arr[mid] > key):
                hi = mid - 1
            else:
                lo = mid + 1
        return False

    n = len(arr)
    for i in range(n):
        b = arr[i]
        a = b + key
        if(binarySearch(arr,a,i+1,n-1)== True):
            return 1
    return 0


if __name__ == "__main__":
    arr = list(map(int,input().split()))
    key = int(input())
    print(returnAns(arr,key))