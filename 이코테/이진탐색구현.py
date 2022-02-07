# 이진 탐색 소스코드 구현(재귀 함수)
def binary_search(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    if array[mid] == target:
        return mid

    elif array[mid] > target:
        binary_search(array, target, start, target - 1)

    else:
        binary_search(array, target, target + 1, end)


    n, target = map(int, input().split())
    array = list(map(int, input().split()))

    result = binary_search(array, target, 0, n - 1)

    if result == None:
        print('원소가 존재하지 않습니다.')
    else:
        print(result + 1)




# 이진 탐색 소스코드 구현(반복문)
def binary_search2(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = target -1
        else:
            start = target + 1

    return None


