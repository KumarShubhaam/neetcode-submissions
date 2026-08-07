class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(i, total, curr):
            # print('for i=', i, curr)
            if total == target:
                # print('append', curr)
                res.append(curr.copy())
                return

            if i >= len(candidates):
                return
            
            # include the ith  element
            curr.append(candidates[i])
            total += candidates[i]
            if total <= target:
                dfs(i+1, total, curr)

            # exclude the ith element
            curr.pop()
            total -= candidates[i]
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1, total, curr)
            

        dfs(0, 0, [])
        return res
