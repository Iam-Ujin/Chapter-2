'''
배열에 주어진 수들을 m번 더하여 가장 큰 수 만들기
배열의 크기 n, 숫자가 더해지는 횟수 m, 연속으로 k번 초과 x
입력
5 8 3
2 4 5 4 6
출력
46
'''

n, m, k = map(int, input().split())
lst = sorted(list(map(int, input().split())), reverse=True)

max = lst[0]
next = lst[1]

a, b = divmod(m, k + 1)
print(a * (k * max + next) + b * max)

# result = 0
# check = 0

# while True:
#     if check >= m:
#         break
#
#     else:
#         for _ in range(k):
#             result += max
#             check += 1
#
#         if check < m:
#             result += next
#             check += 1

# print(result)




