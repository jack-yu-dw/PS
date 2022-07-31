# https://www.acmicpc.net/problem/2231
# 참고) https://jsitclub.tistory.com/59

n = int(input())

result = []

for i in range(n+1):
    d_sum = i
    for j in str(i):
        d_sum += int(j)
    if d_sum == n:
        result.append(i)

if len(result) != 0:
    result.sort()
    print(result[0])
else:
    print(0)