def solve(count,dis,n,q):
    add = 0
    for i in range(26):
        if(count[i] > q):
            add+= count[i]-q
    print(add)



if __name__ == "__main__":
    test = int(input())
    for cases in range(test):
        n,queries = map(int,input().split())
        dis = input()
        count = [0]*26
        for i in range(n):
            count[ord(dis[i])-97] += 1
        for query in range(queries):
            q = int(input())
            solve(count,dis,n,q)