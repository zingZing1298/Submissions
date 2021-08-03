lim,bob = map(int,input().split())

for i in range(100):
    lim = lim * 3
    bob = bob * 2
    if(lim > bob):
        print(i+1)
        break