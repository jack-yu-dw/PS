# p. 감시 피하기
# https://www.acmicpc.net/problem/18428

n = int(input())
map = []
for _ in range(n):
    map.append(list(input().split()))

teacher = 0
for i in range(n):
    for j in range(n):
        if map[i][j] == 'T':
            teacher += 1

# 각 선생에 대하여 해당 선생이 학생을 발견할 수 있는지 확인
def catch_student(x, y):
    catch = False
    # x축에 대해 장애물이 등장할 때까지 확인
    l = y-1
    while l >= 0:
        if map[x][l] == 'S': # 장애물 발견 이전에 학생 발견
            catch = True
            break
        elif map[x][l] == 'O':
            break
        else: # map[x][l] == 'X' or 'T'
            l -= 1
            continue
    r = y+1
    while r < n:
        if map[x][r] == 'S': # 장애물 발견 이전에 학생 발견
            catch = True
            break
        elif map[x][r] == 'O':
            break
        else: # map[x][r] == 'X' or 'T'
            r += 1
            continue
    
    # y축에 대해 장애물이 등장할 때까지 확인
    u = x-1
    while u >= 0:
        if map[u][y] == 'S': # 장애물 발견 이전에 학생 발견
            catch = True
            break
        elif map[u][y] == 'O':
            break
        else: # map[d][u] == 'X' or 'T'
            u -= 1
            continue
    d = x+1
    while d < n:
        if map[d][y] == 'S': # 장애물 발견 이전에 학생 발견
            catch = True
            break
        elif map[d][y] == 'O':
            break
        else: # map[d][y] == 'X' or 'T'
            d += 1
            continue

    return catch # 학생 발견 X ... catch 가 True 이면 학생을 발견한 것 / Fasle 이면 발견하지 못한 것

safe = False
# dfs 로 장애물 세우면서 학생 발견 가능한지 체크
def check(object):
    global safe
    if object == 3:
        count = 0
        for x in range(n):
            for y in range(n):
                if map[x][y] == 'T':
                    if not catch_student(x, y): # 만약 모든 선생들이 학생을 발견하지 못하는 경우가 존재하면
                        count += 1
                        if count == teacher:
                            safe = True # 모든 학생들을 감시로부터 피하도록 할 수 있다
        return
    else:
        for i in range(n):
            for j in range(n):
                if map[i][j] == 'X':
                    map[i][j] = 'O'
                    object += 1
                    check(object)
                    map[i][j] = 'X'
                    object -= 1

check(0)
if safe:
    print("YES")
else:
    print("NO")