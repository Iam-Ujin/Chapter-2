# 프로그래머스 이중우선순위큐
import heapq

def solution(operations):
    answer = []

    for i in operations:
        a, b = i.split()
        if a == 'I':
            heapq.heappush(answer, int(b))
        else:
            if len(answer) > 0:
                if b == '1':
                    answer = heapq.nlargest(len(answer), answer)[1:]
                    heapq.heapify(answer)
                else:
                    heapq.heappop(answer)

    if len(answer) == 0:
        return [0,0]
    else:
        return [heapq.nlargest(len(answer), answer)[0],heapq.heappop(answer)]

