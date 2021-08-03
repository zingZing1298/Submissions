n =int(input())
s = input()
count = 0
res = ""
i = 0
while(i < len(s)):
    res += s[i]
    count += 1
    i = i + count
print(res)