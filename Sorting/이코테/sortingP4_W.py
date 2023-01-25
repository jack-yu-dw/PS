# p.363 카드 정렬하기 (잘못된 풀이)
# https://www.acmicpc.net/problem/1715

n = int(input())
data = []
for _ in range(n):
    data.append(int(input()))

data.sort()
result = 0

if n == 1:
    result = data[0]
if n == 2:
    result = data[0] + data[1]
if n > 2:
    result = data[0] + data[1]
    for i in range(2, n):
        result = result * 2 + data[i] # 잘못된 풀이
        print(result)

print(result)