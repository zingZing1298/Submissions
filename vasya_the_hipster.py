red,blue = map(int,input().split())
cp = 0
cs = 0

if(red > blue):
    red,blue = blue,red
blue = (blue-red)//2
print(red,blue)