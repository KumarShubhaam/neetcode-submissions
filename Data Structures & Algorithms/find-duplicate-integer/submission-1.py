class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        for i,n in enumerate(nums):
            index = abs(n) - 1
            if nums[index] < 0:
                return abs(n)
            nums[index] = -1 * nums[index]

