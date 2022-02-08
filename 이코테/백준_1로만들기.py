'''
1. x가 3으로 나누어 떨어지면 3으로 나누기
2. 2로 나누어 떨어지면 2로 나누기
3. 1 빼기
연산 사용횟수 최솟값 출력
10
3
'''
from collections import deque

n = int(input())
d = [0, 0]

#bfs
def bfs(n):
    count = 0
    queue = deque([(n, count)])

    while queue:
        n, count = queue.popleft()

        if n == 1:
            return count
        if n % 2 == 0:
            queue.append([n//2, count + 1])
        if n % 3 == 0:
            queue.append([n//3, count + 1])

        queue.append([n -1, count+1])

print(bfs(n))







#dp
for i in range(2, n + 1):
    d.append(d[i-1] + 1)
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3] + 1)

print(d[n])


