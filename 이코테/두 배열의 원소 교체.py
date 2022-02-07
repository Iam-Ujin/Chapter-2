'''
배열 A, B n개의 원소로 구성
최대 k번 바꿔치기 연산을 수행할 때 A의 원소의 합이 최대가 되도록
입력
5 3
1 2 5 4 3
5 5 6 6 5
출력
26
'''

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break

print(sum(a))