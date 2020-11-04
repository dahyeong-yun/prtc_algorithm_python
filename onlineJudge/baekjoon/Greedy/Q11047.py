# 왜 이 문제가 Greedy로 해결될 수 있는가? A_i가 A_i-1의 배수이기 때문에
# 1 <= n <= 10
# 1 <= k <= 100,000,000
n, k = map(int, input().split(" "))
count = 0
term = [int(input())]

for _ in range(n-1):
    term.append(int(input()))

for i in range(1, len(term)+1, 1):
    count += k // term[-i]
    k = k % term[-i]

print(count)