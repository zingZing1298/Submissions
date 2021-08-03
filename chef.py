try:
    def returnsPrice(arr,n,k):
        total = sum(arr)
        new = 0
        for i in arr:
            if(i > k):
                new += k
            else:
                new += i
        return (total - new)

    if __name__ == "__main__":
        test = int(input())
        for _ in range(test):
            n,k = map(int,input().split())
            arr = list(map(int,input().split()))
            print(returnsPrice(arr,n,k))

except:
    pass