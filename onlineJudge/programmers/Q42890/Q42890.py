from itertools import combinations


def solution(relation):
    row_count = len(relation)
    col_count = len(relation[0])

    col_raw = [[] for _ in range(col_count)]

    for i in range(row_count):
        for j in range(col_count):
            col_raw[j].extend(combinations(relation[i], j))
    return list(col_raw)
'''
    answer = 0

    for i in range(col_count):
        print(len(set(col_raw[i])), row_count)
        if len(set(col_raw[i])) == row_count:
            answer += 1
    return answer
'''

relation = [["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"],
            ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]

print(solution(relation))