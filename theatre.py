n,m,a = map(int,input().split())
length  = n // a
width = m // a
if(n%a !=0):
    length+= 1
if(m%a != 0 ):
    width += 1
print(length*width,end= "")