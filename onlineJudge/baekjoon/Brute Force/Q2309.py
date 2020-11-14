people = []
for _ in range(9):
    people.append(int(input()))

total = sum(people)
target = total - 100
sorted_people = sorted(people)
target_index = []
# print(sorted_people)

for i in range(9):
    for j in range(0, i+1):
        # print(i,j)
        if sorted_people[i] + sorted_people[j] == target and i != j:
            target_index.append(sorted_people[i])
            target_index.append(sorted_people[j])
    if len(target_index) == 2:
        sorted_people.remove(target_index[0])
        sorted_people.remove(target_index[1])
        break

for i in range(7):
    print(sorted_people[i])