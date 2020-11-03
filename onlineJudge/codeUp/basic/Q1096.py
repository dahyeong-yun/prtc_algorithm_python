coordinate = []
n = int(input())

for i in range(n):
    coordinate.append(list(map(int, input().split())))

go_board = [[0] * 19 for _ in range(19)]

for i in range(n):
    go_board[coordinate[i][0]-1][coordinate[i][1]-1] = 1

for i in range(19):
    for j in go_board[i]:
        print(j, end=" ")
    print()