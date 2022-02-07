'''
4 11
802
743
457
539

200
'''
k, n = map(int, input().split())
array = []
for _ in range(k):
    array.append(int(input()))

start = 0
end = max(array)


while start <= end:
    sum = 0
    mid = (start + end) // 2
    for i in array:
        sum += i // mid
    if sum < n:
        end = mid - 1
    else:
        start = mid + 1

print(end)
