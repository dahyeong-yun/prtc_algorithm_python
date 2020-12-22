string = input()
str_list = [string[i] for i in range(len(string))]
order_count = int(input())
orders = []
cursor = len(str_list)

for _ in range(order_count):
    orders.append(input())

for i in orders:
    if i[0] == "L" and cursor > 0:
        cursor -= 1
    elif i[0] == "B":
        if cursor > 0:
            str_list.pop(cursor - 1)
            cursor -= 1
    elif i[0] == "D" and cursor < len(str_list):
        cursor += 1
    elif i[0] == "P":
        this_order, add_letter = i.split(" ")
        str_list.insert(cursor, add_letter)
        if cursor < len(str_list): cursor += 1

for i in str_list:
    print(i, end="")
