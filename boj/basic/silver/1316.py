# https://www.acmicpc.net/problem/1316

n = int(input())
cnt = 0
for _ in range(n):
    word = input()
    temp = []
    if len(word) != 1:
        group = True
        temp.append(word[0])
        for i in range(1, len(word)):
            if word[i] not in temp:
                temp.append(word[i])
            elif (word[i] in temp) and (word[i-1] != word[i]):
                group = False
                break
            else:
                continue
        if group:
            cnt += 1
    else:
        cnt += 1

print(cnt)


