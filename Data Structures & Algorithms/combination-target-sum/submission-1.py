'''
16
3 = 0,1,2,3,4,5 = 0,3,6,9,12,15
4 = 0,1,2,3,4   = 0,4,8,12,16
5 = 0,1,2,3     = 0,5,10,15

'''
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def helper(i, target, freq_map):
            if target == 0:
                curr = []
                # print(freq_map)
                for n,f in freq_map.items():
                    curr += [n] * f
                res.append(curr)
                return

            if i >= len(nums):
                return
            # print('for', nums[i], 'target=', target, 'map',  freq_map)

            max_freq = target // nums[i]

            for j in range(max_freq+1):
                freq_map[nums[i]] = j
                target -= (nums[i] * j)
                helper(i+1, target, freq_map)
                target += (nums[i] * j)
                del freq_map[nums[i]]

            return

        helper(0, target, {})
        return res


                



