def GCD(a, b):
    if b == 0:
        return a
    else:
        if a > b:
            return GCD(b, a % b)
        else:
            return GCD(a, b % a)


def LCM(a, b):
    k = GCD(a, b)
    return k * (a // k) * (b // k)


for i in range(int(input())):
    n, m = map(int, input().split())
    print(LCM(n, m))
