# p.376 정수 삼각형
# https://www.acmicpc.net/problem/1932

n = int(input())
dp = [[] for _ in range(n)]
for i in range(n):
    data = list(map(int, input().split()))
    dp[i] = data

for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            left = 0
            right = dp[i-1][0]
        elif j == i:
            left = dp[i-1][j-1]
            right = 0
        else:
            left = dp[i-1][j-1]
            right = dp[i-1][j]
        dp[i][j] = dp[i][j] + max(left, right)

result = dp[n-1][:]
print(max(result))
# print(max(dp[n-1])) 로 한번에 출력 가능