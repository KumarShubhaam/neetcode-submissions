class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1 
        max_water = 0
        while l < r:
            water = min(heights[l], heights[r]) * (r - l)
            max_water = max(water, max_water)
            # print('water-', water, '--', heights[l], heights[r])
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        
        return max_water