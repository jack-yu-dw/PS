""" 
개선된 다익스트라 알고리즘
O(ElogV) 의 시간복잡도
'최단 거리가 가장 짧은 노드'를 선택하는 과정을, 다익스트라 최단 경로 함수 안에서 우선순위 큐(최소 힙)를 이용하는 방식으로 대체함.
"""

import heapq # PriorityQueue 보다 heapq 가 통상적으로 조금 더 빠르게 동작한다. (파이썬에서는 최소 heap 이 default)
import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수, 간선의 개수를 입력받기
n, m = map(int, input().split())
# 시작 노드 번호를 입력받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n+1)]
# 방문한 적이 있는지 체크하는 목적의 리스트를 만들기
visited = [False] * (n+1)
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b, c))

# 개선된 다익스트라 알고리즘
def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start)) # (거리, 노드 번호) ... 파이썬의 heapq 라이브러리는 원소로 튜플을 입력받으면 튜플의 첫번째 원소를 기준으로 우선순위 큐를 구성한다. 따라서 (거리, 노드 번호) 순서대로 튜플 데이터를 구성해 우선순위 큐에 넣으면 거리 순으로 정렬된다.
    distance[start] = 0
    while q: # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# 다익스트라 알고리즘 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1):
    # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
    if distance[i] == INF:
        print("INFINITY")
    # 도달할 수 있는 경우, 거리를 출력
    else:
        print(distance[i])


'''
간단한 다익스트라 알고리즘은 '최단 거리가 가장 짧은 노드'를 찾기 위해서 매번 최단 거리 테이블을 선형적으로 탐색해야 했고, 
이 과정에서만 O(V)의 시간이 걸렸음.
하지만 최단 거리가 가장 짧은 노드를 단순히 선형적으로 찾는 것이 아니라 더욱더 빠르게 찾을 수 있다면, 시간 복잡도를 더 줄일 수 있을 것.

개선된 다익스트라 알고리즘에서는 힙(Heap) 자료구조를 사용함.
힙 자료구조를 이용하게 되면 특정 노드까지의 최단 거리에 대한 정보를 힙에 담아서 처리하므로, 출발 노드로부터 가장 거리가 짧은 노드를 더 빠르게 찾을 수 있음.
그리고 이 과정에서 선형 시간이 아닌 로그 시간이 걸리게 됨.
'''