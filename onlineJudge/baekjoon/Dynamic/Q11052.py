n = int(input())
price = [0]
price += list(map(int, input().split(" ")))

max_price = [0] * (n+1)
max_price[1] = price[1]

for i in range(2, len(price)):
    for j in range(1, i+1):
        max_price[i] = max(max_price[i-j] + price[j], max_price[i])

print(max_price[n])