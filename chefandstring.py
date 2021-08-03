try:
    def returnsPair(a):
        n = len(a)
        count = 0
        i = 0
        while(i < n-1):
            if(a[i] =='x' and a[i+1] == 'y'):
                count += 1
                i +=1

            elif(a[i] == 'y' and a[i+1] == 'x'):
                count += 1
                i +=1
            i += 1 
        return count

    if __name__ == "__main__":
        test = int(input())
        for _ in range(test):
            string = input()
            print(returnsPair(string))
except:
    pass
