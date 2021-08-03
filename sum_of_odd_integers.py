import math
def check_sum(n,k):
    flag = 0
    if(n==1 and k==1):
        flag = 1
    if(n%2==0 and k%2==0 and k<=math.sqrt(n)):
        flag = 1
    elif(n%2==1 and k%2==1 and k<=math.sqrt(n)):
        flag = 1
    else:
        flag = 0
    if(flag == 1):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    test = int(input())
    for cases in range(test):
        n,k = map(int,input().split())
        check_sum(n,k)