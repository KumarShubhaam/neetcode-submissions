class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n  = len(heights)
        left = [0 for i in range(n)]
        right = [n-1 for i in range(n)]
        lStack = []
        rStack = []

        l, r = 0, n-1
        while l < n and r > -1:
            if lStack and heights[lStack[-1]] >= heights[l]:
                while lStack and heights[lStack[-1]] >= heights[l]:
                    left[l] = left[lStack.pop()]
            else:
                left[l] = l
            lStack.append(l)
            l += 1

            if rStack and heights[rStack[-1]] >= heights[r]:
                while rStack and heights[rStack[-1]] >= heights[r]:
                    right[r] = right[rStack.pop()]
            else:
                right[r] = r
            rStack.append(r)
            r -= 1

        # print(left, right)
        max_area = 0
        for i in range(n):
            width = right[i] - left[i] + 1
            area = width * heights[i]
            # print('for h', heights[i], '=', area)
            max_area = max(area, max_area)
            area = 0

        return max_area