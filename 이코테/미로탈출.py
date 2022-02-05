'''
n * m
현 위치(1, 1) 출구 (n, m)
한번에 한 칸 씩 이동, 괴물이 있는 부분 0, 괴물이 없는 부분 1
탈출하기 위해 움직여야 하는 최소 칸의 갯수
입력
5 6
101010
111111
000001
111111
111111
출력
10
'''
from collections import deque

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

# 상 하 좌 우
dx = [-1, 1, 0 ,0]
dy = [0, 0, -1, 1]



def bfs(x, y):
    queue = deque([(x, y)])

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 외벽을 벗어날 시 제외
            if nx >= n or nx < 0 or ny >= m or ny < 0:
                continue
            # 길이 아닐 시 제외
            if graph[nx][ny] == 0:
                continue
            # 처음 방문하는 길 일 시 방문체크
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[n - 1][m - 1]

print(bfs(0, 0))