# import time

n = int(input())
order = []
stack = []


def order_classify(order_list):
    order_code = order_list[0]
    if order_code == "push":
        stack.append(order_list[1])
    elif order_code == "pop":
        if len(stack) > 0:
            print(stack[-1])
            stack.pop()
        else: print(-1)
    elif order_code == "top":
        print(stack[-1]) if len(stack) > 0 else print(-1)
    elif order_code == "size":
        print(len(stack))
    elif order_code == "empty":
        print(1) if len(stack) == 0 else print(0)
    else:
        pass


for idx in range(n):
    order.append(list(map(str, input().split(" "))))

for idx in range(n):
    # start_time = time.time()
    order_classify(order[idx])
    # end_time = time.time()


# print("total time : ", end_time - start_time)