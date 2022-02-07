'''
수의 개수 n
내림차순 정렬
입력
3
15
27
12
출력
27 15 12
'''

n = int(input())
array = []

for _ in range(n):
    array.append(int(input()))

for i in sorted(array, reverse=True):
    print(i, end=' ')