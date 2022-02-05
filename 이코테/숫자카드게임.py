import sys
sys.stdin = open('input.txt')
'''
n * m 형태 카드
선택 행의 가장 낮은 수 뽑기(결과적으로 가장 높은 수)
입력
3 3
3 1 2
4 1 4
2 2 2
출력
2
입력
2 4
7 3 1 8
3 3 3 4
출력
3
'''

n, m = map(int, input().split())
result = 0
arr = []
for _ in range(n):
    lst = list(map(int, input().split()))
    arr.append(min(lst))
    max(arr)

print(max(arr))


