k = 1
for i in range(1, int(input())+1):
    k *= i
print(k)

a = b = 1
exec('b *= a; a += 1;' * int(input()))
print(b)