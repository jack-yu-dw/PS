# p.353 인구 이동 (bfs 로도 구현 가능)
# https://www.acmicpc.net/problem/16234

n, l, r = map(int, input().split())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

def available(now, compare):
    if abs(now - compare) >= l and abs(now - compare) <= r:
        return True
    else:
        return False

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[False] * n for _ in range(n)]

# bfs 로 국경선을 열 수 있는지 체크하면서, 만약 열 수 있다면 연합에 추가한다.
def check_border(x, y):
    global countries
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < n and ny >=0 and ny < n:
            if not visited[nx][ny] and available(data[x][y], data[nx][ny]): # 국경선을 열 수 있다면
                countries.append((nx, ny))
                check_border(nx, ny)
    return

def change_population(countries):
    if len(countries) > 1:
        population = 0
        for p in countries:
            population += data[p[0]][p[1]]
        modified = int(population / len(countries))
        for p in countries:
            data[p[0]][p[1]] = modified
        return 1
    else:
        return 0

countries = []
count = 0
while True:
    union_num = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == False:
                countries.append((i, j))
                check_border(i, j)
                union_num += change_population(countries)
                countries.clear()
    if union_num != 0:
        count += 1
    else:
        break
    visited = [[False] * n for _ in range(n)]

print(count)
            
            