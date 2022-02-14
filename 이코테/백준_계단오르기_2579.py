'''
한번에 한 계단 or 두 계단
마지막 계단 무조건 밟기
받을 수 있는 점수의 최댓값
입력
6
10
20
15
25
10
20
출력
75
'''
n = int(input())
array = []
for _ in range(n):
    array.append(int(input()))

d = [0] * n
d[0] = array[0]
d[1] = array[0] + array[1]
d[2] = max(array[0] + array[2], array[1] + array[2])

for i in range(3, n):
    d[i] = max(d[i-3] + array[i-1] + array[i], d[i-2] + array[i])

print(d[n - 1])