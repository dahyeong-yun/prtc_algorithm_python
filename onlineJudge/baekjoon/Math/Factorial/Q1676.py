a = b = 1
exec('b *= a; a += 1;' * int(input()))
txt = str(b)

answer = 0
for i in range(1, len(txt)):
    if txt[-i] == "0":
        answer += 1
    else:
        break

print(answer)