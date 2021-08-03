test = int(input())
for cases in range(test):
    n = int(input())
    arr = list(map(int,input().split()))
    flag,count = 0,0
    one_ind = arr.index(1)
    for i in range(one_ind+1,n):
        if(arr[i] == 0):
            count += 1
        elif(arr[i] == 1 and count<5):
            flag = 1
            break
        elif(arr[i] == 1 and count>= 5):
            flag,count = 0,0
            continue
    if(flag == 1):
        print("NO")
    else:
        print("YES")
            

