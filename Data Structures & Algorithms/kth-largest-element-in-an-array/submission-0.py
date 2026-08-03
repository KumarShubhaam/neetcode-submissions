class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-1*n for n in nums]
        heapq.heapify(nums)
        res = 0
        for i in range(k):
            res = heapq.heappop(nums)
        return -1*res