n = int(input())

exclude = [1 for i in range(n)]
expense = []
selected = []

for i in range(n):
    expense.append(list(map(int, input().split())))

for i in range(len(expense)):
    minimum = min(expense[i])
    selected.append(minimum)

    selected_before = expense[i].index(minimum)
    if i < len(expense) - 1: expense[i+1][selected_before] = 1001

print(sum(selected))
