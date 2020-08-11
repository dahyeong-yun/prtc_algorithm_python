# 17269
cnt = list(map(int,input().split(" ")))
names = list(map(str, str(input()).upper().split(" ") ))
line = [3,2,1,2,4,3,1,3,1,1,3,1,3,2,1,2,2,2,1,2,1,1,1,2,2,1]

length = len(names[0]) if len(names[0]) >= len(names[1]) else len(names[1])

fit_num = []
for i in range(0, length) :
    if i < cnt[0] :
        fit_num.append(line[ord(names[0][i])-65])
    if i < cnt[1] :
        fit_num.append(line[ord(names[1][i])-65])
# 글자 만들기

tmp_num = []

while len(fit_num) > 2 :
    tmp_len = len(fit_num)-1
    # print("tmp_len", tmp_len)
    for i in range(0, tmp_len) :
        # print(i)
        tmp_num.append( (fit_num[i] + fit_num[i+1])%10 )        
    fit_num = []
    fit_num = tmp_num
    tmp_num = []

fit_str = str(fit_num[1]) if fit_num[0] == 0 else str(fit_num[0])+str(fit_num[1])
print("{}%".format(fit_str))