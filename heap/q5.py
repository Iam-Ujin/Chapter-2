# 프로그래머스 디스크 컨트롤러
import heapq

def solution(jobs):
    answer = 0
    end, i = 0, 0
    start = -1
    heap = []

    # jobs의 길이 만큼 반복
    while i < len(jobs):
        for j in jobs:
            # start < jobs의 요소 index 1 < end 이면
            if start < j[0] <= end:
                # j의 요소를 반대로 힙에 푸시
                heapq.heappush(heap, [j[1], j[0]])
        # 힙의 길이가 0 보다 크먄
        if len(heap) > 0:
            # now 는 힙팝
            now = heapq.heappop(heap)
            # start에 end값 넣기
            start = end
            # end에 현재 pop된 요소의 인덱스 0(길이)
            end += now[0]
            # answer 에 (현재 위치 - 현재요소의 작업 요청시간)을 더한다
            answer += end - now[1]
            i += 1
        else:
            end += 1
    # 모든 요청에서 종료까지 시간을 다해 갯수만틈 나누기
    return int(answer / len(jobs))