n = int(input()) # 자리 수
count = 0
if n == 1:
    print(9) # n이 1일 땐 9개 전부
elif n > 1:
    for i in range(10**(n-1), 10**n): # 10의 n-1 승 부터 10의 n승 -1 까지
        sum = 0
        #print("i가 {} 일 때 : ".format(i), end="")
        str_num = str(i)
        for j in range(len(str_num)-1):
            #print(str_num[j], str_num[j+1], end="")
            sum += abs(int(str_num[j]) - int(str_num[j+1]))
        if sum == n-1: # 각 자리수의 차의 합이 n-1
            #print(" {}는 계단수".format(i))
            count += 1
    print(count%1000000000)