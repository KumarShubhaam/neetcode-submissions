class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        r0 = [1,2,3,4,5,6]
        r1 = [6,1,2,3,4,5]
        r2 = [5,6,1,2,3,4]
        r3 = [4,5,6,1,2,3]
        r4 = [3,4,5,6,1,2]
        r5 = [2,3,4,5,6,1]

        r0 = [1,2,3,4,5]
        r1 = [5,1,2,3,4]
        r2 = [4,5,1,2,3]
        r3 = [3,4,5,1,2]
        r4 = [2,3,4,5,1]
        '''
        l, r = 0, len(nums)-1
        ans = 1001
        while l <= r:
            if nums[l] <= nums[r]:
                return nums[l]
            # elif nums[l] > nums[r]:
            else:
                l += 1