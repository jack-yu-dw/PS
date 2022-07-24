# https://www.acmicpc.net/problem/2577

a = int(input())
b = int(input())
c = int(input())

n = str(a*b*c)

result = [0 for i in range(10)]

for i in range(len(n)):
    result[int(n[i])] += 1

for i in range(len(result)):
    print(result[i])
