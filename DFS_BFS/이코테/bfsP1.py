# p.339 특정 거리의 도시 찾기
# https://www.acmicpc.net/problem/18352

from collections import deque

n, m, k, x = map(int, input().split())

graph = [[] for i in range(n+1)]
visited = [False] * (n+1)
distance = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

queue = deque()
queue.append(x)
visited[x] = True
while queue:
    now = queue.popleft()
    for i in graph[now]:
        if not visited[i]:
            queue.append(i)
            visited[i] = True
            distance[i] = distance[now] + 1

if k not in distance:
    print(-1)
else:
    for i in range(1, len(distance)):
        if distance[i] == k:
            print(i)
