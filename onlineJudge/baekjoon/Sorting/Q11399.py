n = int(input()) # 사람의 수 < 1000
draw_time = sorted(list(map(int, input().split(" ")))) # < 1000

result = [0] * n

for i in range(n):
    # print(i,"번째 사람", end=" ")

    for j in range(i+1):
        result[i] += draw_time[j]

    # print(result[i],"초")


print(sum(result))