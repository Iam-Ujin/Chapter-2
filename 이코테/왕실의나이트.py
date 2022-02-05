'''
8 * 8 
1. 수평 2칸 이동 뒤 수직 1칸
2. 수직 2탄 이동 뒤 수평 1칸
나이트가 이동할 수 있는 경우의 수 출력
행 1 ~ 8
열 a ~ h
입력 a1 출력 2
'''

# print(ord('a'), ord('b'), ord('c'))
data = input()
row = int(data[1])
col = int(ord(str(data[0])) - 96)

moves = [(1, 2), (-1, 2), (1, -2), (-1, -2), (2, 1), (-2, 1), (2, -1), (-2, -1)]
result = 0

for move in moves:

    nrow = row + move[0]
    ncol = col + move[1]
    if 0 < ncol <= 8 and 0 < nrow <= 8:
        result += 1

print(result)
