# https://www.acmicpc.net/problem/9093

n = int(input())

for _ in range(n):
    line = list(map(list, input().split()))
    for i in line:
        print("".join(i[::-1]), end=" ")