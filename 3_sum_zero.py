
def threeSum(self, a):
    n = len(a)
    a.sort()
     final = []
      dct = {}
       for i in range(n-1):
            c = a[i]
            p1, p2 = i+1, n-1
            while(p1 < p2):
                if(a[p1]+a[p2] == -1*c):
                    if((c, a[p1], a[p2]) not in dct):
                        dct[(c, a[p1], a[p2])] = 1
                    p1 += 1
                    p2 -= 1
                elif(a[p1]+a[p2] < -1*c):
                    p1 += 1
                else:
                    p2 -= 1
        final = dct.keys()
        return list(final)


if __name__ == "__main__":
    arr = list(map(int,input().split()))
    print(sol(arr,len(arr)))
