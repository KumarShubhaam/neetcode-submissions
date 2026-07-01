class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compliment = {}
        for i in range(len(nums)):
            n = nums[i]
            c = target - n
            if c in compliment.keys():
                i1 = compliment[c]
                return [i, i1] if i < i1 else [i1, i]
            compliment[n] = i