# p.360 안테나 (시간 초과 / 메모리 초과)
# https://www.acmicpc.net/problem/18310

n = int(input())
house = list(map(int, input().split()))
house.sort()

min = 1e9
result = 0
for i in house: # 안테나 설치 집
    distance = 0
    for j in house:
        if i < j:
            distance += j-i
        elif i > j:
            distance += i-j
    if distance < min:
        min = distance
        result = i

print(result)