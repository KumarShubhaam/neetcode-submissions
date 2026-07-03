class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i,n in enumerate(nums):
            count = 1
            for j,m in enumerate(nums):
                if j != i:
                    count *= m
            output.append(count)

        return output
