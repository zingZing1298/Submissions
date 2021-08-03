p = input()
p = p.casefold()
vowels = ['a','e','i','o','u','y']
new = []
for i in range(len(p)):
    if p[i] not in vowels:
        new.append(p[i])
for i in range(len(new)):
    print('.'+new[i],sep = "",end="")