n = int(input())
x = 0
while(n>0):
    s = input()
    if(s == 'X++' or s == '++X' ):
        x += 1
    elif(s == 'X--' or s == '--X'):
        x -= 1
    
    n -= 1
print(x)
