import sys
sys.stdin = open('input.txt')
'''
1. n에서 1을 뺀다.
2. n을 k로 나눈다.
n이 1이 될 때까지 수행해야하는 최소 횟수
입력
25 5
출력
2
'''
n, k = map(int, input().split())
result = 0

while n > 1:
    if n % k != 0:
        n -= n % k
        result += n % k
    else:
        n //= k
        result += 1


print(result)