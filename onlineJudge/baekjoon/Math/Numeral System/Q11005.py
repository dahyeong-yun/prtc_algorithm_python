def dec2(n, b):
    char = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # print(len(char))
    a = []
    while (n != 0):
        a.append(char[n % b])
        n //= b
    return ''.join(a[::-1])


n, b = map(int, input().split())
print(dec2(n, b))
