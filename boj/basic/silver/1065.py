# https://www.acmicpc.net/problem/1065

def han(x):
    if x < 100:
        return True
    else:
        a = x // 100
        b = (x - a * 100) // 10
        c = x % 10
        if b - a == c - b:
            return True

n = int(input())
cnt = 0
for i in range(1, n+1):
    if han(i):
        cnt += 1

print(cnt)
