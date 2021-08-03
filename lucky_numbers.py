
def lucky(n):
    flag = 0
    res = 0
    while(n>0):
        res = n%10
        flag = 0
        if(res == 4 or res== 7):
            flag = 1
        else:
            flag = 0
            break
        n = n//10
    if(flag == 1):
        return True
    else:
        return False

def almostLucky(n):
    flag = 0
    if(lucky(n)):
        print('YES')
        
    else:
        for i in range(n+1):
            if(lucky(i)):
                if(n%i == 0):
                    flag = 1
                    break
                else:
                    flag = 0
        if(flag == 1):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    n = int(input())
    almostLucky(n)