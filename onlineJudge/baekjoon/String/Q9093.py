text = []
n = int(input())
for _ in range(n):
    text.append(list(map(str, input().split(" "))))

for i in range(n):
    for str in text[i]:
        print(''.join(reversed(str)), end=" ")
    print()
