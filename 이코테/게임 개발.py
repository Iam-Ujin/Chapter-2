import sys
sys.stdin = open('input.txt')
'''
n * m 
(A, B) A: 북쪽으로부터 B: 서쪽으로부터
바다 x
1. 현재 방향 기준 왼졲방향부터
2. 왼쪽 방향에 가보지 않은 칸 존재 > 왼쪽 방향 회전 > 한 칸 전진
            가보지 않은 칸 x   > 왼쪽 장향 회전 > 1단계
3. 네 방향 모두 가본 칸 or 바다 > 바라보는 방향 유지 한 칸 뒤로 > 1단계
                                                    > 뒤가 바다면 멈춤
'''
n, m = map(int, input().split())
x, y, d = map(int, input().split())


graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

graph[x][y] = 1
count = 1
dir_count = 0

while True:
    d -= 1
    if d < 0:
        d = 3

    nx = x + dx[d]
    ny = y + dy[d]

    # 왼쪽 방향에 가보지 않은 칸이 있으면 전진
    if graph[nx][ny] == 0:
        graph[nx][ny] = 1
        x, y = nx, ny
        # 방문 칸 + 1
        count += 1
        # 회전 횟수 초기화
        dir_count = 0
        continue
    # 그렇지 않으면 회전 횟수 + 1
    else:
        dir_count += 1
    # 4 방향 다 돌았을 시 뒤로, 회전 횟수 초기화
    if dir_count == 4:
        nx = x - dx[d]
        ny = y - dy[d]
        dir_count = 0

        # 뒤에 가보지 않은 칸이 있을 경우에만 후진, 없으면 break
        if graph[nx][ny] == 0:
            x, y = nx, ny
        else:
            break

print(count)