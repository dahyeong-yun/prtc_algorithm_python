def solution(n):
    # 다중 배열 생성
    # 1000 이므로 3중 for문 까지도 가능 1,000,00 0,000 (10억번)

    # 피라미드 크기
    maxnum = n * (n + 1) // 2  # 피라미드에 들어가는 제일 큰 수

    print(maxnum)
    # 행렬 초깃값
    row = 0
    col = 0

    # 피라미드 생성 n * n
    pyramid = [[0] * n for _ in range(n)]

    # 방향 : 방향은 3가지 방향이 있음
    direction = "topdown"  # bottomup, leftright
    # 방향을 바꾸는 기준, 0이 아니거나 배열의 범위를 벗어날 때

    # 위에서 아래로
    for i in range(maxnum):
        # print(i+1, row, col)
        pyramid[row][col] = i + 1

        if direction == "topdown":
            row += 1
            if row > n - 1 or pyramid[row][col] > 0:
                direction = "leftrigth"
                row -= 1
                col += 1
        elif direction == "bottomup":
            row -= 1
            col -= 1
            if row < 0 or col < 0 or pyramid[row][col] > 0:
                direction = "topdown"
                row += 2
                col += 1
        elif direction == "leftrigth":
            col += 1
            if col > n - 1 or pyramid[row][col] > 0:
                direction = "bottomup"
                row -= 1
                col -= 2

    answer = []
    for i in range(n):
        for j in range(n):
            if pyramid[i][j] > 0:
                answer.append(pyramid[i][j])

    return answer