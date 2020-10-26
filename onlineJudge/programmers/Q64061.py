# https://programmers.co.kr/learn/courses/30/lessons/64061

def solution(board, moves):
    stack = []
    rows, cols = len(board), len(board)
    pang_count = 0

    # move
    moves_count_from_zero = [moves[idx] - 1 for idx in range(len(moves))]

    for idx in range(len(moves)):
        for row in range(rows):

            if board[row][moves_count_from_zero[idx]] != 0:
                stack.append(board[row][moves_count_from_zero[idx]])
                if len(stack) >= 2 and stack[-1] == stack[-2]:
                    stack.pop()
                    stack.pop()
                    pang_count += 2

                board[row][moves_count_from_zero[idx]] = 0
                break

    # answer = 1
    return pang_count
