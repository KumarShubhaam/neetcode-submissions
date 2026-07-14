class Solution:
    def findMin(self, nums: List[int]) -> int:

        l, r = 0, len(nums)-1
        ans = 1001
        while l <= r:
            if nums[l] <= nums[r]:
                return nums[l]
            # elif nums[l] > nums[r]:
            else:
                l += 1