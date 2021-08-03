try:
    def firstDigit(n):
        while n >= 10:
            n = n / 10
        return int(n)


    def lastDigit(n):
        return (n % 10)

    test = int(input())
    for _ in range(test):
        n = int(input())
        s = firstDigit(n) + lastDigit(n)
        print(s) 


except:
    pass
