from collections import defaultdict
'''
입력
4 5 1
1 2
1 3
1 4
2 4
3 4
출력
1 2 4 3
1 2 3 4
입력
5 5 3
5 4
5 2
1 2
3 4
3 1
출력
3 1 2 5 4
3 1 4 2 5
'''

# 노드, 간선, 시작노드
n, m, v = map(int, input().split())
graph = defaultdict(list)
# range(m)인 이유:  간선의 갯수 = 들어오는 입력값의 수 ( 양방향 간선 )
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
# 인점한 노드가 여러 개 일 때, 작은 노드부터 방문해야 함 > 오름차순 정렬
for node in list(graph):
    graph[node] = sorted(graph[node])

# 재귀 dfs
def recursive_dfs(v, discovered=[]):
    discovered.append(v)
    # 노드v의 인접 노드
    for i in graph[v]:
        # 가 방문하지 않은 노드일 시
        if i not in discovered:
            # 재귀
            discovered = recursive_dfs(i, discovered)
    return discovered



def bfs(v):
    queue, discovered = [v], [v]
    # 큐가 존재할 때까지
    while queue:
        v = queue.pop(0)
        # 노드v의 인접 노드
        for i in graph[v]:
            # 가 방문하지 않은 노드일 시
            if i not in discovered:
                discovered.append(i)
                queue.append(i)
    return discovered

print(' '.join(map(str, recursive_dfs(v))))
print(' '.join(map(str, bfs(v))))


