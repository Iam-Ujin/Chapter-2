# 원점에서 k번째로 가가운 점
# 입력 >>>> points = [[1, 3], [-2, 2]],  k = 1
# 출력 >>>> [[-2, 2]]
# 입력 >>>> points = [[3, 3], [5, -1], [-2, 4]],  k = 2
# 출력 >>>> [[3, 3], [-2, 4]]
import heapq


def kCloset(self, points: List[List[int]], k: int) -> List[List[int]]:
    dists = []
    heap = []
    for point in points:
        dist = point[0] ** 2 + point[1] ** 2
        heapq.heappush(heap, dist)
        dists.append(dist)

    kth_dist = [heapq.heappop(heap) for _ in range(k)][-1]

    return [points[idx] for idx, dist in enumerate(dists) if dist <= kth_dist]