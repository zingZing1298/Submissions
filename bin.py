def returns_x(n):
    for i in range(1,n):
        binary = bin(n//i)
        print(binary)






if __name__ == '__main__':
    test = int(input())
    for cases in range(test):
        n = int(input())
        returns_x(n)