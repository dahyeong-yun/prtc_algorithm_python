import math

n, s = map(int, input().split(" "))  # 동생 명 수, 현재 위치
a = list(map(int, input().split(" ")))  # 동생 위치

abs_distance = list(set([abs(s - i) for i in a]))

if n >= 2:
    k = math.gcd(abs_distance[0], abs_distance[1])
    for i in range(2, len(abs_distance)):
        k = math.gcd(abs_distance[i], k)
    print(k)
elif n == 1:
    print(abs_distance[0])
