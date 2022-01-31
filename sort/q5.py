# 백준 11650 좌표정렬하기
import sys
input = sys.stdin.readline

n = int(input())
array = []

for i in range(n):
    [x, y] = map(int, input().split())
    array.append([x, y])

array.sort()

for i in range(n):
    print(array[i][0], array[i][1])


# 백준 11650 좌표정렬하기 -2
import sys
input = sys.stdin.readline

n = int(input())
array = []

for i in range(n):
    [x, y] = map(int, input().split())
    array.append([y, x])

array.sort()

for i in range(n):
    print(array[i][1], array[i][0])




