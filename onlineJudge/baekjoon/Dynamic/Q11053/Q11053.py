n = int(input())
num_list = list(set(list(map(int, input().split()))))
print(len(num_list))

temp = 0
partial = []
for i in range(len(num_list)):
    if num_list[i] > temp :
        partial.append(num_list[i])
        temp = num_list[i]
    elif num_list[i] < temp:
        partial
