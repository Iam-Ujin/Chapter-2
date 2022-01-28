from collections import deque

from dfs_bfs.prac import dfs_recursive, dfs_stack


assert dfs_recursive(1, []) == [1, 2, 5, 6, 7, 3, 4]
assert dfs_stack(1) == [1, 4, 3, 5, 7, 6, 2]



def island_dfs_stack(grid):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    rows, cols = len(grid), len(grid[0])
    cnt = 0

    for row in range(rows) :
        for col in range(cols) :
            if grid[row][col] != '1' :
                continue

            cnt += 1
            stack = [(row,col)]

            while stack:
                x, y = stack.pop()
                grid[x][y] = '0'
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if nx < 0 or ny < 0 or nx >= rows or ny >= cols or grid[nx][ny] != '1' :
                        continue
                    stack.append((nx,ny))
    return cnt



def bfs_queue(start):
    visited = [start]
    q = deque([start])

    while q :
        node = q.popleft()
        for adj in graph[node] :
            if adj not in visited:
                q.append(adj)
                visited.append(adj)

    return visited



def island_bfs(grid) :
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    rows, cols = len(grid), len(grid[0])
    cnt = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] != '1':
                continue

            cnt += 1
            q = deque([(row, col)])

            while q :
                x, y = q.popleft()
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if nx < 0 or nx >= rows or ny < 0 or ny >= cols or grid[nx][ny] != '1' :
                        continue

                    grid[nx][ny] = '0'
                    q.append((nx,ny))

    return  cnt