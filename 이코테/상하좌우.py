import sys
sys.stdin = open('input.txt')

'''
n * n 정사각형
시작 좌표 (1, 1)
공간 밖은 무시
최종 도착 지점 좌표 공백으로 구분하여 출력
출력
3 4
'''
n = int(input())
lst = input().split()
x, y = 1, 1
direction = ['L', 'R', 'U', 'D']
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


for elem in lst:
    for i in range(4):
        if elem == direction[i]:
            nx = x + dx[i]
            ny = y + dy[i]
            if nx <= n and nx > 0 and ny <= n and ny > 0:
                x = nx
                y = ny
            break
print(x, y)