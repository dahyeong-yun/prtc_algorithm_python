n = int(input())
house_location = sorted(list(map(int, input().split(" "))))
print(house_location[(n-1)//2])


'''
house_location_sorted = sorted(house_location)

lowest_idx = 0
min_distance = 200000

for idx, val in enumerate(house_location_sorted):
    sum_distance = 0

    for j in house_location_sorted:
        sum_distance += j - val if j > val else val - j

    if min_distance > sum_distance:
        lowest_idx = idx
        min_distance = sum_distance

print(house_location_sorted[lowest_idx])
'''