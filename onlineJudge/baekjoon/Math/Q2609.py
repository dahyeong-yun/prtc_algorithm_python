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
    return k * (a//k) * (b//k)


n, m = map(int, input().split())

print(GCD(n, m))
print(LCM(n, m))

# [ ] 유클리드 호제법 증명