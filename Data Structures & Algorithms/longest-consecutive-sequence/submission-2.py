class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        high = -10**9
        low = 10**9
        seen = set()
        for n in nums:
            seen.add(n)
            high = max(high, n)
            low = min(low, n)

        ans = 0
        temp = 0
        # s = []
        for i in range(low, high+1):
            if i not in seen:
                temp = 0
                # s = []
            else:
                temp += 1
                # s.append(i)
                ans = max(ans, temp)
        # print(s)
        return ans