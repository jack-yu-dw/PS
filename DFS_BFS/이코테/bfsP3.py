# p.344 경쟁적 전염
# https://www.acmicpc.net/problem/18405

from collections import deque

n, k = map(int, input().split())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

temp = []
for i in range(n):
    for j in range(n):
        if data[i][j] != 0:
            temp.append((data[i][j], i, j))

temp.sort()

q = deque()
for t in temp:
    q.append((t[1], t[2], t[0]))

sec, x, y = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

temp_q = deque()
for s in range(sec):
    while q:
        a, b, number = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                if data[nx][ny] == 0:
                    data[nx][ny] = number
                    temp_q.append((nx, ny, number))

    while temp_q:
        q.append(temp_q.popleft())

print(data[x-1][y-1])