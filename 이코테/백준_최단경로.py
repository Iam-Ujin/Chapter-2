'''
정점의 게수 v, 간선의 개수 e
둘째 줄에 시작 정점의 번호 k
셋째 줄부터 e개의 줄에 각 간선을 나타내는 세개의 정수(u, v, w)
u에서 v로 가는 가중치 w인 간선

첫째 줄부터 v개의 줄에 걸쳐, i번째 줄에 i번 정점으로의 최단경로의 경로값 출력
시작점 자신은 0으로 경로가 존재하지 않는 경우 INF출력

0
2
3
7
INF

'''
import sys
sys.stdin = open('input.txt')

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드 갯수, 간선 갯수
v, e = map(int, input().split())
# 시작 노드 번호
start = int(input())
graph =[[] for _ in range(v + 1)]
# 최단 거리 테이블 초기화
distance = [INF] * (v + 1)

for _ in range(e):
    u, v, w = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c
    graph[u].append((v, w))
    distance[start] = 0


q = [(0, start)]
# 시작 노드로 가기 위한 최단 거리는 0으로 설정 > 큐에 삽입

while q:
    # 가장 최단 거리가 짧은 노드 정보 꺼내기
    dist, node = heapq.heappop(q)
    # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
    if distance[node] < dist:
        continue
    # 현재 노드와 연결된 다른 인접한 노드들을 확인
    for next_dist, next_node in graph[node]:
        cost = dist + next_node
        if cost < distance[next_dist]:
            distance[next_node] = cost
            heapq.heappush(q, (cost, next_node))


# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, v + 1):
    # 도달할 수 없는 경우 무한(INFINITY)
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])