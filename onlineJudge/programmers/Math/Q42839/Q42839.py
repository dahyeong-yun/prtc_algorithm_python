from itertools import permutations

scale = 10000000
prime_checker = [i for i in range(scale + 1)]
prime_checker[1] = 0

for i in range(2, int(scale ** 0.5) + 1):
    if prime_checker[i] != 0:
        for j in range(2, (scale // i) + 1):
            prime_checker[i * j] = 0

def solution(numbers):
    global prime_checker
    answer = []
    comb = []
    num_len = len(numbers)
    
    # 모든 조합 구하기
    for i in range(num_len):
        comb.extend(map(''.join, permutations(numbers, i+1)))

    int_comb = []
    for i in comb:
        if i[0] == '0' and len(i) > 1:
            int_comb.append(int(i[1:]))
        else:
            int_comb.append(int(i))

    set_int_comb = set(int_comb)
    for i in set_int_comb:
        if prime_checker[i] != 0:
            answer.append(i)

    return len(answer)

print(solution("0012111"))