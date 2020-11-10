def dynamic(n): # 1<= n <= 1000
    if n == 1:
        return 1
    elif n == 2:
        return 3

    dp = [0] * (n + 1)

    dp[0] = 0
    dp[1] = 1
    dp[2] = 3

    for i in range(3, n + 1, 1):
        dp[i] = dp[i - 1] + (dp[i - 2] * 2)

    return dp[n] % 10007


print(dynamic(int(input())))
