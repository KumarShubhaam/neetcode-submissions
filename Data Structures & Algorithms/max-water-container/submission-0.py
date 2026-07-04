class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        max_water = 0
        for i1,h1 in enumerate(heights):
            for i2 in range(1, n):
                h2 = heights[i2]
                # print(i1, i2, '--', h1, h2)
                water = min(h1, h2) * (i2 - i1)
                # print('water', water, '-->', i1, i2)
                max_water = max(max_water, water)

        return max_water