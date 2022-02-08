'''
선택적 약탈하여 식량을 빼앗을 때 최댓값 구하기
인접한 식량창고 약탈 x
입력
4
1 3 1 5
출력
8
'''
n = int(input())
array = list(map(int, input().split()))

d = [0] * n
d[0] = array[0]
d[1] = max(array[0], array[1])

for i in range(2, n):
    d[i] = max(d[i - 1], d[i - 2] + array[i])

print(d[n - 1])
