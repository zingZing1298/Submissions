def sol(arr,n):
    flag = 0
    o = 1
    while o < len(arr): 
        if(arr[o] < arr[o - 1]): 
            flag = 1
        o += 1
    if(not flag):
        return -1
    else:
        start = 0
        end = n-1
        #starting the start pointer to find the first out of sort element index
        for start in range(0,n-1):
            if(arr[start] > arr[start+1]):
                break
        
        
        #start end pointer to the find the end element of subarray
        for end in range(n-1,-1,-1):
            if(arr[end] < arr[end-1]):
                break
        
        #max1,min1 are local maxima and minima of subarray to arr[start]
        max1 = arr[start]
        min1 = arr[start]

        #find new minima and maxima of subarray
        for i in range(start+1,end+1):
            if(arr[i]>max1):
                max1 = arr[i]
            if(arr[i]<min1):
                min1 = arr[i]

        # increment start to find the bigger subarray which has to be sorted
        for i in range(0,start):
            if(arr[i] > min1):
                start = i
                break
        # similarly find the end of the bigger subarray which has to be sorted
        i = n-1
        while i >= end+1:
            if(arr[i]<max1):
                end = i
                break
            i -= 1
                
        #return indices
        return [start,end]

if __name__ =="__main__":
    n = int(input())
    arr = list(map(int,input().split()))
    print(sol(arr,n))