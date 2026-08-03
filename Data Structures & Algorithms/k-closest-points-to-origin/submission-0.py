import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def calc_distance(x, y):
            return math.sqrt(x**2 + y**2)

        d = {}
        heap = []
        for x,y in points:
            dist = calc_distance(x, y)
            if dist in d:
                d[dist].append([x,y])
            else:
                d[dist] = [[x,y]]
            heapq.heappush(heap, dist)

        res = []
        for i in range(k):
            cord = d[heapq.heappop(heap)].pop()
            res.append(cord)
        return res