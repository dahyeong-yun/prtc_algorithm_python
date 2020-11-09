n = int(input())  # 보드의 크기
board = [[0] * n for _ in range(n)]  # 보드 생성

k = int(input())  # 사과의 크기
for _ in range(k):  # 사과의 위치
    x, y = map(int, input().split(" "))
    board[x - 1][y - 1] = 1

timing = {0: "N"}  # 방향 초기 값
l = int(input())  # 방
for _ in range(l):
    sec, direction = input().split(" ")
    timing[int(sec)+1] = direction


def exist_apple(x, y):
    global board
    if board[x][y] == 1:
        return True
    return False


def next_coordinate(order, x, y):
    global board
    global history
    result_x = x
    result_y = y

    if order == "E":
        result_y += 1
    elif order == "S":
        result_x += 1
    elif order == "W":
        result_y -= 1
    elif order == "N":
        result_x -= 1

    return result_x, result_y


def move_snake(x, y):
    global board
    global history

    if not exist_apple(x, y):
        board[history[0][0]][history[0][1]] = 0  # 꼬리가 변경
        history.pop(0)
    board[x][y] = 4  # 머리가 움직임
    history.append([x, y])


def 벽에_닿았는가_판단(x, y):
    global n
    if x >= n or x < 0 or y >= n or y < 0:
        return True
    else:
        return False


def 몸에_닿았는가_판단(x, y):
    global board
    if board[x][y] == 4:
        return True
    return False


direction_list = ["E", "S", "W", "N"]
direction = direction_list[0]

is_wall = False
is_body = False
current_x, current_y = 0, 0  # 시작점
history = [[current_x, current_y]]
board[current_x][current_y] = 4  # 뱀 모양
sec: int = 0  # 시간


def direction_change(current_direction, change_order):
    global direction_list
    current_index = direction_list.index(current_direction)
    if change_order == "D":
        return direction_list[current_index + 1 if (current_index + 1) < 3 else 0]
    elif change_order == "L":
        return direction_list[current_index - 1 if (current_index - 1) >= -4 else 0]


while not is_wall and not is_body:
    sec += 1  # 초를 증가

    if sec in timing.keys():  # 방향이 바뀌는지 체크
        direction_change_order = timing[sec]
        direction = direction_change(direction, direction_change_order)

    next_x, next_y = next_coordinate(direction, current_x, current_y)

    if 벽에_닿았는가_판단(next_x, next_y):
        break
    is_body = 몸에_닿았는가_판단(next_x, next_y)

    current_x, current_y = next_x, next_y
    move_snake(current_x, current_y)

print(sec)
for i in board:
    for j in i:
        print(j, end= " ")
    print()