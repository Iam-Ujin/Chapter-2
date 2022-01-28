# 배열의 k번째 큰 수
import heapq

# 최소힙을 음수로 전환하여 풀이
def fideKthLargest1(self, nums: List[int], k: int) -> int:
    heap = list()
    for n in nums:
        # n을 음수로 전환하여 삽입
        heapq.heappush(heap, -n)

    for _ in range(k):
        heapq.heappop(heap)

    # 결과 값에 - 를 붙여서 양수로 리턴
    return -heap.heappop(heap)


# heap 모듈을 이용한 풀이
def fideKthLargest2(self, nums: List[int], k: int) -> int:
    # return heapq.nlargest(k, nums)[-1]
    heapq.heapify(nums)
    for _ in range(len(nums) - k):
        heapq.heappop(nums)

    return heapq.heappop(nums)

# 정렬
def fideKthLargest3(self, nums: List[int], k: int) -> int:
    return sorted(nums, reverse=True)[k-1]
