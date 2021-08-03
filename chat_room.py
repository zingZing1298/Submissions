a = input()
b = "hello"
letter_count, j = 0,0
for i in range(len(a)):
    if(a[i] == b[j]):
        j += 1
        letter_count += 1

        if(letter_count == 5):
            break

if(letter_count == 5):
    print("YES")
else:
    print("NO")