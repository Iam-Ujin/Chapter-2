'''
5
4 1 5 2 3
5
1 3 7 9 5

1
1
0
0
1
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
    result = binary_tree(n_array, i, 0, n -1)
    if result != None:
        print(1)
    else:
        print(0)