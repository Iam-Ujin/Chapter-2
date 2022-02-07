'''
매장 내 부품 n개
list
손님이 문의한 부품 m
list
부품이 있으면 yes 없으면 no
5
8 3 7 9 2
3
5 7 9

'''

n = int(input())
n_array = sorted(list(map(int, input().split())))
m = int(input())
m_array = list(map(int, input().split()))

def binary_tree(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif mid > target:
            end = mid - 1
        else:
            start = mid + 1

    return None

for i in m_array:
    result = binary_tree(n_array, i, 0, n-1)
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')
