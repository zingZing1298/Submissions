n = int(input())
for i in range(n):
    p = input()
    if(len(p)<= 10):
        print(p)
    else:
        print(p[0]+ '%d'%(len(p)-2) + p[-1])

