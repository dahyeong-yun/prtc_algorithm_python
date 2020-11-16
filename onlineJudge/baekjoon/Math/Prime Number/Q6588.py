scale = 1000000
prime_checker = [i for i in range(scale + 1)]
prime_checker[1] = 0

for i in range(2, int(scale ** 0.5) + 1):
    if prime_checker[i] != 0:
        for j in range(2, (scale // i) + 1):
            prime_checker[i * j] = 0

while True:
    k = int(input())
    if k == 0:
        break
    else:
        temp = []
        for a in range(3, (k//2)+1):
            if prime_checker[k - prime_checker[a]] != 0:
                print("{} = {} + {}".format(k, a, k-a))
                temp.append(a)
                temp.append(k-1)
                break
        if len(temp) == 0:
            print("Goldbach's conjecture is wrong")
        temp = []