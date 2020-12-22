n = int(input())
k = []
for i in range(n):
    k.append(int(input()))

highest = max(k)

dp = [0] * (highest+1)

dp[0] = 0
dp[1] = 1
dp[2] = 2
dp[3] = 4


for j in range(4, highest+1, 1):
    dp[j] = dp[j-1] + dp[j-2] + dp[j-3]

for i in k: print(dp[i])