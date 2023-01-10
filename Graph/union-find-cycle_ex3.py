""" 
서로소 집합을 활용한 (무방향)사이클 판별 알고리즘.

서로소 집합은 무방향 그래프 내에서의 사이클을 판별할 때 사용할 수 있음. (방향 그래프에서의 사이클 여부는 DFS 를 이용하여 판별 가능)
해당 알고리즘은 그래프에 포함되어 있는 간선의 개수가 E개일 때 모든 간선을 하나씩 확인하며,
매 간선에 대하여 union 및 find 함수를 호출하는 방식으로 동작함. (방향성이 없는 무방향 그래프에서만 적용 가능)
"""

# 특정 원소가 속한 집합을 찾기 (Find)
def find_parent(parent, x):
    # root 노드가 아니라면, root 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기 (Union)
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(union 연산)의 개수 입력받기
v, e = map(int, input().split())
parent = [0] * (v+1) # 부모 테이블 초기화

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

cycle = False # 사이클 발생 여부

for i in range(e):
    a, b = map(int, input().split())
    # 사이클이 발생한 경우 종료
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    # 사이클이 발생하지 않았다면 합집합(Union) 수행
    else:
        union_parent(parent, a, b)

if cycle:
    print("사이클이 발생했습니다.")
else:
    print("사이클이 발생하지 않았습니다.")