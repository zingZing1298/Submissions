try:
    def returnsA(s,n):
        a = []
        for i in range(n):
            if(i % 2== 0 and i!=n-1):
                a.append(s[i])
            elif(i == n-1):
                a.append(s[i])
        return "".join(a)

    if __name__ == '__main__':
        test = int(input())
        for _ in range(test):
            s = input()
            print(returnsA(s,len(s)))
except:
    pass