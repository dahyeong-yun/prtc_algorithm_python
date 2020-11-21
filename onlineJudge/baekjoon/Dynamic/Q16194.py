n = int(input())
price = [0]
price += list(map(int, input().split(" ")))

min_price = price

for i in range(2, len(price)):
    for j in range(1, i+1):
        # print("i : {}, j : {}".format(i,j))
        min_price[i] = min(min_price[i-j] + price[j], min_price[i])

print(min_price[n])