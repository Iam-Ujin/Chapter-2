'''
손님이 요청한 총 길이 m
m만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 높이의 최댓값 구하기
입력
4 6
19 15 10 17
출력
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