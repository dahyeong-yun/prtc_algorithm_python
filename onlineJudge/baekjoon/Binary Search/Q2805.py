n, m = map(int,input().split(" ")) # 나무의 수, 가져가려는 길이이
trees = list(map(int, input().split(" ")))

left = 1
right = max(trees)

while left <= right :
    mid = (left + right) // 2

    cut = 0
    for i in trees:
        if mid < i:
            cut += i - mid

    if cut >= m:
        left = mid + 1
    else: # cut < m
        right = mid - 1

print(right)