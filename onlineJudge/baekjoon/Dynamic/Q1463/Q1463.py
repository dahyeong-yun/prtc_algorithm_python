n = int(input())

# index를 순번으로 사용하기 위해 n+1 만큼의 리스트 생성
count = [0 for _ in range(n+1)]

for idx in range(2, n+1):
    if idx % 3 == 0 and count[idx // 3] < count[idx-1]:
        count[idx] = count[idx // 3] + 1
    elif idx % 2 == 0 and count[idx // 2] < count[idx-1]:
        count[idx] = count[idx // 2] + 1
    else:
        count[idx] = count[idx-1] + 1

print(count[n])