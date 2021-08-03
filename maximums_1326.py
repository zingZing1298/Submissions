def maximum(n,arr):
    x = []
    x.append(0)
    for i in range(n):
        for j in range(i):
            max_val = max(arr[i],arr[j])
    
    
    print(*x)





if __name__ == "__main__":
    n = int(input())
    arr = list(map(int,input().split()))
