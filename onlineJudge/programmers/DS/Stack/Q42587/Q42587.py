def solution(priorities, location):
    answer = 0
    max_num = max(priorities)
    while True:
        pop_num = priorities.pop(0)
        if pop_num == max_num:
            answer += 1        # 꺼낸 횟 수
            if location == 0:  # 찾고자 하는 수의 위치를 꺼내면 종료
                break
            else:
                location -= 1  # 찾고자 하는 수의 위치가 아니라면, 수가 하나 빠졌으니, 현재 위치가 1 작아짐
            max_num = max(priorities) # 최대 값 초기화
        else:
            priorities.append(pop_num)
            if location == 0: # 현재 위치가 원래 빠지는 수였다면, 끝으로 수가 갔으니 '길이 - 1'
                location = len(priorities) - 1
            else:
                location -= 1 # 뒤로 가는 수가 현재 수가 아니므로 앞으로 한칸 보낸 셈
    return answer


print(solution([2, 1, 3, 2], 2))
# 1 3 2 2
# 3 2 2 1
print(solution([1, 1, 9, 1, 1, 1, ], 5))

# https://eda-ai-lab.tistory.com/461
# https://n1tjrgns.tistory.com/190