
def noOfSwaps(arr,n):
    count = 0
    rem_i = []
    new_i = []
    res,new = 0,0
    for i in range(n):
        rem_i.append(i%2)
        new_i.append(arr[i] % 2)
       
    for i in range(n):
        res = res ^ (i%2)
        new = new ^ (arr[i]%2)
    #print(rem_i,new_i)
        
    if(new > res):
        return -1
       
    else:
        for i in range(n):
            if(rem_i[i] != new_i[i]):
                count += 1      
        return count//2

def returnsCount(arr,n):
    even,odd = 0,0
    for i in range(n):
        if(i%2 ==0 and arr[i]%2!=0):
            even += 1
        elif(i%2!=0 and arr[i]%2 ==0):
            odd += 1
    if(even == odd):
        return even
    else:
        return -1


if __name__ == '__main__':
    test = int(input())
    for _ in range(test):
        n = int(input())
        arr = list(map(int,input().split()))
        print(returnsCount(arr,n))


