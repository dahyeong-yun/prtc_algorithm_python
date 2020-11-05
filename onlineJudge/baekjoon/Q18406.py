number_raw = input()
number_list = []
for i in range(len(number_raw)):
    number_list.append(int(number_raw[i]))

sum = 0
k = len(number_list) // 2 # 가운데 인덱스
for i in range(k):
    sum += number_list[i]

for j in range(k, len(number_list), 1):
    # print(j, end=" ")
    sum -= number_list[j]

if sum == 0:
    print("LUCKY")
else:
    print("READY")