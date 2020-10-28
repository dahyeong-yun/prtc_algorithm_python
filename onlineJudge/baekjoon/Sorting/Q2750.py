n = int(input())
arr = set([])
for i in range(n):
    arr.add(int(input()))

answer = sorted(list(arr))

for i in answer: print(i)