def sol(arr,n):
    ans = -1
    count = [False for i in range(n+1)]
    for i in range(n):
        if(count[arr[i]] == False):
            count[arr[i]] = True
        else:
            ans = i
            print(arr[i])
            return
            

if __name__ == "__main__":
    #test = int(input())
    #for cases in range(test):
    arr = list(map(int,input().split()))
    sol(arr,len(arr))