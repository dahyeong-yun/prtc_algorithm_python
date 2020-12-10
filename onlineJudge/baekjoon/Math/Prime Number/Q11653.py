target = int(input())
i = 2

while target != 1:
    if target % i == 0:
        print(i)
        target //= i
    else:
        i += 1