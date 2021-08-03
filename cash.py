cash = ['1','5','10','20','100']
n = int(input())
count = 0
while (n > 0):
    for i in range(len(cash),0):
        if n >= cash[i]:
            count += n/cash[i]
            if n % i == 0:
                break
        else:
            n -= n/cash[i] * cash[i]
    print(count)
