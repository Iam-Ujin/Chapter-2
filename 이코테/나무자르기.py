'''
4 7
20 15 10 17

15
'''
n, m = map(int, input().split())
array = list(map(int, input().split()))

start = 0
end = max(array)


while start <= end:
    length = 0
    mid = (start + end) // 2
    for i in array:
        if i > mid:
            length += i - mid

    if length < m:
        end = mid - 1
    else:
        start = mid + 1

print(end)