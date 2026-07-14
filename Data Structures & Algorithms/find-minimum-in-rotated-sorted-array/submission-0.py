class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        ans = 1001
        while l <= r:
            ans = min(ans, nums[r], nums[l])
            l += 1
            r -= 1

        return ans
        