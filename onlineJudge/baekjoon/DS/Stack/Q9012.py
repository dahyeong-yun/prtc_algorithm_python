n = int(input())
parenthesis = []
result = ""
expect = "("

for _ in range(n):
    parenthesis.append(input())

for string in parenthesis:
    stack = []
    result = "YES"
    for idx in range(len(string)):
        if "(" == string[idx]:
            stack.append(string[idx])
        elif ")" == string[idx]:
            if len(stack) != 0:
                stack.pop()
            else:
                result = "NO"
                break
    if len(stack) != 0:
        result = "NO"
    stack = []
    print(result)