def com(arr,x,n):
    temp = [0] * n
    combinations(arr,temp,0,x-1,0,n)

def returnsflag(flag):
    if(flag == 1):
        print("Yes")
    else:
        print("No")
    return

def combinations(arr,temp,begin,end,index,n):
    add,flag = 0,0
    exit = 0
    if(index == n):
        if(exit == 0):
            for j in range(n):
                add += temp[j]
                #print(temp[j],end = " ")
                #print("sum:",add)
            if(c-d <= add <= c+d):
                flag = 1
                returnsflag(flag)
                
            return
        else:
            return
            
    i = begin
    while(i <= end and end -i +1 >= n-index):
        temp[index] = arr[i]
        combinations(arr,temp, i+1, end, index+1, n)
        i += 1
    


if __name__ == "__main__":
    #test = int(input())
    #for cases in range(test):
        
    n,a,b,c,d = map(int,input().split())
        #if((c-d <= n*(a-b) <= c+d) or (c-d <= n*(a+b) <= c+d)):
            #print("Yes")
        #elif:
    arr = [int(i) for i in range(a-b,a+b+1)]
    print("arr:",*arr)
    com(arr,len(arr),n)
    