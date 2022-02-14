import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드 갯수, 간선 갯수
n, m = map(int, input().split())
# 시작 노드 번호
start = int(input())
graph =[[] for _ in range(n + 1)]
# 방문체크
visited = [False] * (n + 1)
# 최단 거리 테이블 초기화
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c
    graph[a].append((b, c))


# 방문하지 않은 노드 중 가장 최단거리가 짧은 노드의 번호 반환
def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i

    return index

def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[[j[0]]] = j[1]
    # 시작노드를 제외한 전체 n-1개의 노드에 대해 반복
    for i in range(n - 1):
        now = get_smallest_node()
        visited[now] = True
        # 현재 노드와 연결된 다른 노드 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 경로가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n + 1):
    # 도달할 수 없는 경우 무한(INFINITY)
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])