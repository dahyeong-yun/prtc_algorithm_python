n = int(input())
score = [list(input().split(" ")) for _ in range(n)]

score.sort(key=lambda each: [-int(each[1]), int(each[2]), -int(each[3]), each[0]])
for i in score:print(i[0])
