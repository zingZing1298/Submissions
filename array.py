def generate_even(n):
    even = []
    for i in range(2,n+1,2):
        even.append(i)
    return even

def generate_odd(n):
    odd = []
    for i in range(1,n,2):
        odd.append(i)
    return odd
   

if __name__ == "__main__":
    test = int(input())
    for cases in range(test):
        n = int(input())
        flag = 0
        if(n == 2):
            print("NO")
        else:   
            even = generate_even(n)
            evesum = sum(even)
            odd = generate_odd(n)
            oddsum = sum(odd)
            diff = evesum - oddsum
            if(diff % 2 == 0):
                flag = 1
                odd[-1] += diff

            if(flag == 1):
                print('YES')
                print(*even,*odd)
            elif(flag == 0):
                print('NO')