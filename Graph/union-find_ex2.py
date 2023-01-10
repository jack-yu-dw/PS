""" 
개선된 서로소 집합 (Union-Find) 알고리즘.

find 함수를 재귀적으로 호출한 뒤에 부모 테이블값을 갱신하는 '경로 압축 (path compression)' 기법을 적용하여 시간 복잡도 개선.
각 노드에 대하여 find 함수를 호출한 이후에, 해당 노드의 root 노드가 바로 부모 노드가 된다.
결과적으로 경로 압축 기법을 이용하게 되면 root 노드에 더욱 빠르게 접근할 수 있다는 점에서 기존의 기본적인 알고리즘보다 시간 복잡도가 개선됨.
"""

# 특정 원소가 속한 집합을 찾기 (Find) : 경로 압축 기법
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

# union 연산을 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합 출력
print("각 원소가 속한 집합: ", end="")
for i in range(1, v+1):
    print(find_parent(parent, i), end=' ')

print()

# 부모 테이블 내용 출력
print("부모 테이블: ", end="")
for i in range(1, v+1):
    print(parent[i], end=' ')