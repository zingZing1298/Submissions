def sol_max(n,arr):
    max_count,min_count = 1,n
    i=0
    count = 1
    while(i<n): 
        if( i+1<n and arr[i+1]- arr[i] <= 2 ):
            count += 1
            i += 1
            
        else:
            i += 1
            if(count<min_count):
                min_count = count
            count = 1   
        if(max_count<count):
                max_count = count     
    print(min_count,max_count)
            
if __name__ == '__main__':
    test = int(input())
    for cases in range(test):
        n= int(input())
        arr = list(map(int,input().split()))
        sol_max(n,arr)