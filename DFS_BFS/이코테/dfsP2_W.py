# p.341 연구소 (대략적인 풀이는 생각했으나 구현을 하지 못함)
# https://www.acmicpc.net/problem/14502

n, m = map(int, input().split())

graph = [] # 초기 맵 리스트
temp = [[0] * m for _ in range(n)] # 벽 3개를 설치한 뒤의 맵 리스트

for _ in range(n):
    data = list(map(int, input().split()))
    graph.append(data)
            
# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0

# DFS 를 이용하여 바이러스 퍼지게 하기
def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx, ny)

# 현재 맵에서 안전 영역의 크기 계산
def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score

# DFS 를 이용하여 벽을 설치하면서, 매번 안전 영역의 크기를 계산
def dfs(count):
    global result
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = graph[i][j]
        
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)
        
        result = max(result, get_score())
        return
    
    else:
        for i in range(n):
            for j in range(m):
                if graph[i][j] == 0:
                    graph[i][j] = 1
                    count += 1
                    dfs(count)
                    graph[i][j] = 0
                    count -= 1

dfs(0)
print(result)