# https://www.acmicpc.net/problem/3052

data = []
for _ in range(10):
    data.append(int(input()))

result = []
for i in range(len(data)):
    data[i] %= 42
    if data[i] not in result:
        result.append(data[i])

print(len(result))
