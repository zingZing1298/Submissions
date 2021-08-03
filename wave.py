def waveSort(arr,n):
    arr.sort()
    for i in range(0,n-1,2):
        arr[i],arr[i+1] = arr[i+1],arr[i]
    return arr

if __name__ == "__main__":
    test = int(input())
    for cases in range(test):
        arr = list(map(int,input().split()))
        n = len(arr)
        print(waveSort(arr,n))


