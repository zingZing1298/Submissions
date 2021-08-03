def sol(arr,n):
    arr[n-1] += 1
    rem = arr[n-1]//10
    arr[n-1] = arr[n-1] % 10

    for i in range(n-2,-1,-1):
        if(rem == 1):
            arr[i] += 1
            rem = arr[i]//10
            arr[i] = arr[i] % 10
    
    if(rem == 1):
        arr.insert(0,1)
    
    while(arr[0] == 0):
        arr.remove(0)
    return arr

#adding to number
if __name__ == "__main__":
    test = int(input())
    for cases in range(test):
        arr = list(map(int,input().split()))
        print(sol(arr,len(arr)))


'''
[0 0 1] + 1 = [ 0 0 2]
[1 2 9]+1 = [ 1 3 0]
[2 9 9]+1 = [3 0 0]
[9 9 9]+1 = [10 10 10] =~ [1 0 0 0]
'''