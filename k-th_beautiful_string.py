test = int(input())
for cases in range(test):
    n,k = map(int,input().split())
    str_a = 'a'
    str_b = 'b'
    res = ''
    p = (n*(n-1))//2
    if(k == 1):
        res = 'a' * (n-2)
        res = res + str_b
        res = res + str_b
        print(res)
    if(k==p):
        res = 'a' * (n-2)
        res = str_b + res
        res = str_b + res
        print(res)
    else:
        res = 'a' * (n-2) 
        count = 1
        while(k > count):
            k = k - count
            count += 1
        x = count 
        count = n - count- 1
        check = res 
        check = check[:count] + 'b' + check[count:]   
        count = count +(x-k + 1)
        check = check[:count] + 'b' + check[count:]
        print(check)

    
