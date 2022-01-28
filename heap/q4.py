# 프로그래머스 더맵게
import heapq

def solution(scoville, k):
    answer = 0
    heapq.heapify(scoville)

    # while scoville[0] < k:
    #     if len(scoville) <= 1:
    #         return -1
    #     else:
    #         min1 = heapq.heappop(scoville)
    #         min2 = heapq.heappop(scoville)
    #         heapq.heappush(scoville, min1 + 2*min2)
    #         answer += 1

    while True:
        min1 = heapq.heappop(scoville)
        if min1 >= k:
            break
        if len(scoville) == 0:
            return -1
        min2 = heapq.heappop(scoville)
        heapq.heappush(scoville, min1 + 2 * min2)
        answer += 1

    return answer