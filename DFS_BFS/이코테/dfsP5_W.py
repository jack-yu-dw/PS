# p.349 연산자 끼워 넣기 (풀이 고안 못함)
# https://www.acmicpc.net/problem/14888

n = int(input())
num = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

min_value = 1e9
max_value = -1e9

def dfs(i, now):
    global min_value, max_value, add, sub, mul, div
    if i==n:
        min_value = min(min_value, now)
        max_value = max(max_value, now)
        return
    else:
        if add > 0:
            add -= 1
            dfs(i+1, now + num[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i+1, now - num[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i+1, now * num[i])
            mul += 1
        if div > 0:
            div -= 1
            if now < 0:
                tmp = abs(now) // num[i]
                dfs(i+1, tmp*-1)
            else:
                dfs(i+1, int(now / num[i]))
            div += 1

dfs(1, num[0])
print(max_value, min_value)