import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드 갯수, 간선 갯수
n, m = map(int, input().split())
# 시작 노드 번호
start = int(input())
graph =[[] for _ in range(n + 1)]
# 최단 거리 테이블 초기화
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 거리는 0으로 설정 > 큐에 삽입
    heapq.heappush((q, (0, start)))
    distance[start] = 0
    while q:
        # 가장 최단 거리가 짧은 노드 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n + 1):
    # 도달할 수 없는 경우 무한(INFINITY)
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])