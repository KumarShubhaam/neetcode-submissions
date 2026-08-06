class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]

        subset = self.subsets(nums[1:])

        res = subset[:]
        for sub in subset:
            res.append(([nums[0]] + sub))

        return res

        