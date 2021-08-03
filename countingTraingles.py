def countTraingles(arr):
    arr.sort()
    count = 0
    n = len(arr)
    for i in range(n-1,0,-1):
        p1 = 0
        p2 = i-1
        while(p1<p2):
            if(arr[p1]+arr[p2] > arr[i]):
                count += p2 - p1
                p2 -= 1
            else:
                p1 += 1
    return count

if __name__ == "__main__":
    arr = list(map(int,input().split()))
    print(countTraingles(arr))