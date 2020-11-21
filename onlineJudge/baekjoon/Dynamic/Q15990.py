div = 1000000009  # div: 방법의 수를 나누는 값
limit = 100000  # limit: 정수 n의 최댓값

dp = [[0 for _ in range(4)] for _ in range(limit + 1)]
dp[1][1] = dp[2][2] = dp[3][3] = dp[3][1] = dp[3][2] = 1;

for i in range(4, limit + 1):
    for j in range(1, 4):
        if j == 1:
            dp[i][j] = dp[i - 1][2] + dp[i - 1][3];
        elif j == 2:
            dp[i][j] = dp[i - 2][1] + dp[i - 2][3];
        else:
            dp[i][j] = dp[i - 3][1] + dp[i - 3][2];
    dp[i][j] %= div;

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    ans = 0
    for i in range(1, 4):
        ans += dp[n][i]
        ans %= div
    print(ans)