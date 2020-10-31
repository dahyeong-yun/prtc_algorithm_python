# 피보나치 구하는 함수
def fiboonacci(num):
    output = 1
    before1 = before2 = 1

    if num == 0:
        output = 0
    elif num == 1 or num == 2:
        output = 1
    else:
        for i in range(num - 2):
            before1 = before2  # 1 1 2
            before2 = output  # 1 2 3
            output = before1 + before2  # 2 3

    return output


T = int(input())  # 테스트케이스의 수

for i in range(T):
    N = int(input())
    if N >= 2:
        a = fiboonacci(N - 1)
        b = fiboonacci(N)
    elif N == 1:
        a = 0
        b = 1
    elif N == 0:
        a = 1
        b = 0
    print(a, b)