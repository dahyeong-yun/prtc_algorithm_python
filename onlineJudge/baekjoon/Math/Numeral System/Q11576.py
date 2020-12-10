a, b = map(int, input().split())
k = int(input()) - 1
a_num = list(map(int, input().split()))

normal_num = 0
for i in range(len(a_num)):
    normal_num += (a ** k) * a_num[i]
    k -= 1

char = "0123456789ABCDEFGHIJKLMNOPQRST" # 30진법 까지만

def dec2(n, b):
    global char
    a = []
    while(n!=0):
        a.append(char[n % b])
        n //= b
    return ''.join(a[::-1])

print_num = dec2(normal_num, b)

for i in range(len(print_num)):
    print(char.index(print_num[i]), end=" ")