def count_n(number, n):
    cnt = 0
    while number != 0:
        number //= n
        cnt += number
    return cnt


m, n = map(int, input().split(" "))

five = count_n(m, 5) - count_n(n, 5) - count_n((m - n), 5)
two = count_n(m, 2) - count_n(n, 2) - count_n((m - n), 2)

print(min(five, two))
