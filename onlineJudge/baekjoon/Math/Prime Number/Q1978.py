n = int(input())
num_list = list(map(int, input().split(" ")))
scale = max(num_list)

prime_checker = [i for i in range(scale+1)]
prime_checker[1] = 0

for i in range(2, int(scale**0.5)+1):
    if prime_checker[i] != 0:
        for j in range(2, (scale//i)+1):
            prime_checker[i*j] = 0

count = 0

for i in num_list:
    # print("i =", i)
    # print("prime_checker[i] :", prime_checker[i])
    if prime_checker[i] != 0:
        count += 1

# print(prime_checker)
print(count)