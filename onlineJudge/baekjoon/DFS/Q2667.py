''' 입력 '''

n = int(input()) # 지도의 크기
square_map = []

for i in range(n):
    square_map.append(list(map(int, input())))

''' 입력 '''
_house_count = 0
house = []
bundle = 0


def dfx(x, y):
    global _house_count
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False

    if square_map[x][y] == 1:

        square_map[x][y] = 2
        _house_count += 1

        dfx(x, y - 1)
        dfx(x, y + 1)
        dfx(x + 1, y)
        dfx(x - 1, y)

        return True
    return False


for i in range(n):
    for j in range(n):
        if dfx(i, j):
            house.append(_house_count)
            _house_count = 0
            bundle += 1

print(bundle)

for i in sorted(house):
    print(i)