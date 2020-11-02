'''
- 입국심사를 기다리는 사람 1 < n명 < 1,000,000,000
- 각 심사관이 한명을 심사하는데 걸리는 시간 리스트 times
  - 심사관의 수  1 < len(times) < 100,000
  - 심사관 마다 걸리는 시간 1 < times[n] < 1,000,000,000


Test Case 1
n = 6, times = [7, 10]

7   1 7분  1 7분  1 7분 1 7분
10  1 10분 1 10분

7 * 4
10 * 2

7 * 3
10 * 3

7 * 2
10 * 4
'''


def solution(n: int, times: list) -> int:
    answer = []

    max_time = max(times)

    min_take_time = 1
    max_take_time = max_time * n

    while min_take_time <= max_take_time:
        mid_take_time = (min_take_time + max_take_time) // 2

        take_men = 0
        for i in times:
            take_men += mid_take_time // i

        if take_men < n:
            min_take_time = mid_take_time + 1
        elif take_men >= n:
            answer.append(mid_take_time)
            max_take_time = mid_take_time - 1

    return min(answer)


print(solution(2, [1,2,3]))