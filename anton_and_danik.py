n = int(input())
s = input()
ca = s.count('A')
cd = s.count('D')

if(ca > cd):
    print("Anton")
elif(cd > ca):
    print("Danik")
elif(cd == ca):
    print("Friendship")