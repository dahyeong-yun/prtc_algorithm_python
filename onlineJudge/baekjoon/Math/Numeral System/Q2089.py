
n = int(input())
sign = 1
if n == 0:
    print(0)
else:
    answer = []
    while n != 0:
        k = n % -2
        if k != 0:
            answer.append(1)
            n -= sign
        else:
            # print(k,n)
            answer.append(0)
        sign *= (-1)
        n //= 2

    for i in range(len(answer), 0, -1):
        print(answer[i-1], end="")
