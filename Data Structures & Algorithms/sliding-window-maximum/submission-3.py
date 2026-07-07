class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        r = 0
        m = 0
        maximum = float('-inf')
        while r < k-1:
            if nums[r] >= maximum:
                maximum = nums[r]
                m = r
            r += 1

        l = 0
        res = []
        while r < len(nums):
            if nums[r] > nums[m]:
                m = r

            w  = nums[l:r+1]
            res.append(nums[m])
            # print('w =', w, res, m)
            r += 1
            if m == l:
                temp = l + 1
                m += 1
                while temp <= l+k and r < len(nums):
                    if nums[temp] >= nums[m]:
                        m = temp
                    temp += 1
            l += 1
            

        return res