def solve(arr,n):
    for i in range(0,n):
        arr[i] += (arr[arr[i]]%n)*n
    for i in range(0,n):
        arr[i] = arr[i]//n 
    print(arr)



if __name__ == "__main__":
    n = int(input())
    arr = list(map(int,input().split()))
    solve(arr,n)