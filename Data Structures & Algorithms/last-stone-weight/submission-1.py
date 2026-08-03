import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for n in stones:
            heapq.heappush(heap, -1*n)

        while len(heap) >= 2:
            s1 = -1 * heapq.heappop(heap)
            s2 = -1 * heapq.heappop(heap)
            new_s = abs(s1 - s2)
            if new_s != 0:
                heapq.heappush(heap, -1*new_s)
        if len(heap) == 0:
            return 0
        return -1 * heapq.heappop(heap)            
        