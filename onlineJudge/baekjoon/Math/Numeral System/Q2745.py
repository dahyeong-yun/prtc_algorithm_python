char = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

word, b = input().split()
base = int(b)
n = []

for i in range(len(word)-1, -1, -1):
    n.append(word[i])

result = 0
for i in range(len(n)):
    multiple = char.index(n[i])
    result += (base ** i) * multiple

print(result)