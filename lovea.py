s = input()
ca = 0
cx = 0
for i in range(len(s)):
    if(s[i] == 'a'):
        ca += 1
    else:
        cx += 1
    
if(ca > len(s)//2):
    print(len(s))    
else:
    print(len(s)- abs(ca-cx) - 1)
