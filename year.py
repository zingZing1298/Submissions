n,m = map(int,input().split())
s = list(map(str,input().split()))
t = list(map(str,input().split()))
q = int(input())

for i in range(q):
    y = int(input())
    print(s[y%n -1]+t[y%m -1])