class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]

        subans = self.permute(nums[1:])
        top = nums[0]
        res = []
        for sub in subans:
            # print('sub', sub)
            for i in range(len(sub)+1):
                temp = sub[:i] + [top] + sub[i:]
                # print('temp =', temp, i)
                res.append(temp)

        return res

                
        