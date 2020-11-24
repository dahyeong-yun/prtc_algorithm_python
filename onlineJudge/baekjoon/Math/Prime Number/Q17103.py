scale = 1000000
prime_checker = [i for i in range(scale + 1)]
prime_checker[1] = 0

for i in range(2, int(scale ** 0.5) + 1):
    if prime_checker[i] != 0:
        for j in range(2, (scale // i) + 1):
            prime_checker[i * j] = 0

for _ in range(int(input())):
    count = 0
    k = int(input())
    for a in range(2, (k//2)+1):
        if prime_checker[k - prime_checker[a]] != 0:
            count += 1
    print(count)
