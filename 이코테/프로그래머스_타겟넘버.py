def solution(numbers, target):
    answer = 0
    queue = [[numbers[0], 0], [-numbers[0], 0]]
    n = len(numbers)

    while queue:
        number, idx = queue.pop()
        idx += 1

        if idx < n:
            queue.append([number + numbers[idx], idx])
            queue.append([number - numbers[idx], idx])
        else:
            if number == target:
                answer += 1

    return answer