def sol(n):
    arr = [[] for i in range(n+1)]

    if(n==0):
        return [1]
    
    elif(n == 1):
        arr[0] = [1]
        arr[1] = [1,1]
        return arr[1]
    
    elif(n == 2):
        arr[0] = [1]
        arr[1] = [1,1]
        arr[2] = [1,2,1]
        return arr[2]
    else:
        arr[0] = [1]
        arr[1] = [1,1]
        i = 2
        while(i <= n):
            arr[i].append(1)
            j = 1
            while(j < len(arr[i-1])):
                arr[i].append(arr[i-1][j] + arr[i - 1][j -1])
                j+=1
            arr[i].append(1)
            i+=1
    return arr[n]
        
if __name__ == "__main__":
    n = int(input())
    print(sol(n))