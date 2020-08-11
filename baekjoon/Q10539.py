n = input()
score =  list(map(int, input().split(" ")))
answer = []

sum = 0
for idx in range(0, len(score)) :
    # print("idx :",idx)
    each = score[idx] * (idx+1) - sum
    sum += each
    print(each, end=" ")
    #answer.append(each)
    
# print(answer)