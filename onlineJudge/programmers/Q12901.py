# https://programmers.co.kr/learn/courses/30/lessons/12901


def solution(a, b):
    # 1-1, 1-2
    # 1-3
    day_name = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    month_last_day = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    whole_day = 0
    # 전체 일 수 계산
    if a > 1:
        for month in range(a - 1):
            # print("month : ", month)
            whole_day += month_last_day[month]
    whole_day += b
    # print("whole_day : ",whole_day)
    # 나머지 계산
    remainder = (whole_day - 2) % 7
    return day_name[remainder - 1]