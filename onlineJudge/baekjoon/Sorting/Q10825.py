def con(n, base):
    a = '0123456789ABCDEF'
    re = ''
    while n > 0:
        n, r = divmod(n, base)
        re = a[r] + re
    return re

def dec2(n, b):
    char = "0123456789ABCDEF"
    a = []
    while(n!=0):
        a.append(char[n % b])
        n //= b
    return ''.join(a[::-1])

orgin_num = int(input(), 2)
# print(con(orgin_num, 8))
print(dec2(orgin_num, 8))