from itertools import combinations


def GCD(a, b, *args):
    if b == 0:
        return a
    else:
        if a > b:
            return GCD(b, a % b)
        else:
            return GCD(a, b % a)


loop = int(input())

for _ in range(loop):
    iterable_list = list(map(int, input().split(" ")))
    answer = 0
    for i in combinations(iterable_list[1:], 2):
        answer += GCD(i[0], i[1])
    print(answer)
    iterable_list = []
    answer = 0