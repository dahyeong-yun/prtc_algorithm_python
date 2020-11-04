number_raw = input()

count_one = 0
count_zero = 0

if int(number_raw[0]) == 0:
    count_zero += 1
else:
    count_one += 1

number_list = [number_raw[0]]

for i in range(1, len(number_raw), 1):
    if number_raw[i] != number_raw[i-1]:

        number_list.append(number_raw[i])

        if int(number_raw[i]) == 0:
            count_zero += 1
        else:
            count_one += 1


print(min(count_zero, count_one))