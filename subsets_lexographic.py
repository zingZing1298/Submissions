def subsets(arr,subset,idx):
    if(len(subset) >0 ):
        print(subset)

    for i in range(idx,n):
        subset.append(arr[i])
        subsets(arr,subset,i+1)
        subset.pop(-1)
    return


def sol(arr,n):
    subset = []
    subsets(arr,subset,0)

if __name__ == "__main__":
    test = int(input())
    for cases in range(test):
        n = int(input())
        arr = list(map(int,input().split()))
        arr.sort()
        sol(arr,n)