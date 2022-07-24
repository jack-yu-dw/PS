# https://www.acmicpc.net/problem/2562
# 참고) https://riley.tistory.com/15

datas = []
for _ in range(9):
    data = int(input())
    datas.append(data)

max = datas[0]
idx = 1
for i in range(1, len(datas)):
    if datas[i] > max:
        max = datas[i]
        idx = i+1

print(max)
print(idx)