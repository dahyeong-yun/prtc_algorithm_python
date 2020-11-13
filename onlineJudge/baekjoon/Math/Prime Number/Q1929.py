m, n = map(int, input().split(" "))
scale = n+1

prime_checker = [i for i in range(scale)]
prime_checker[1] = 0

# print("int(scale**0.5) =", int(scale**0.5))
# print("(scale//int(scale**0.5))+1 =", (scale//int(scale**0.5))+1)

for i in range(2, int(scale**0.5)+1):
    if prime_checker[i] != 0:
        for j in range(2, (scale//i)+1):
            if i*j < len(prime_checker):
                prime_checker[i*j] = 0

for i in range(m, scale):
    if prime_checker[i] != 0:
        print(prime_checker[i])
