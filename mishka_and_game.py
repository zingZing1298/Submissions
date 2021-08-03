c=0;
for i in range(int(input())):
    x,y=map(int,input().split())
    c+=x>y
    c-=x<y
print('Friendship is magic!^^' if c==0 else ['Mishka','Chris'][c<0])