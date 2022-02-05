'''
n * m
구멍 0, 칸막이 1
구멍이 둟려 있는 부분끼리 상, 하, 좌, 우 붙어있는 경우 연결되어 있는 것
생성되는 총 아이스크림 갯수
입력
4 5
00110
00011
11111
00000
출력
3
'''

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))



def dfs(x, y):

    if x < 0 or x >= n or y < 0 or y >= m:
        return False

    if graph[x][y] == 0:

        graph[x][y] = 1
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False


result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)