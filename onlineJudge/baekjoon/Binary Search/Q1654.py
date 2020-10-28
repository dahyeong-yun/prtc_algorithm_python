n, m = map(int,input().split(" ")) # 랜선의 갯 수, 필요한 랜선의 갯수
cable_lengths = []

for i in range(n): cable_lengths.append(int(input()))

min_unit = 1
max_unit = max(cable_lengths)

while min_unit <= max_unit :
    cut_unit = (min_unit + max_unit) // 2

    cut_piece = 0
    for cable_length in cable_lengths:
        if cut_unit <= cable_length:
            cut_piece += cable_length // cut_unit

    if cut_piece >= m:
        min_unit = cut_unit + 1
    else: # cut < m
        max_unit = cut_unit - 1

print(max_unit)