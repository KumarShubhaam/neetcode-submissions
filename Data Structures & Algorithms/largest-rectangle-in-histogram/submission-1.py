class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n  = len(heights)
        stack = []     # (startIndex, height)
        max_area = 0
        for i,h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                max_area = max(max_area, (height * (i - index)))
                start = index

            stack.append((start, h))

        while stack:
            i, h = stack.pop()
            max_area = max(max_area, (h*(n-i)))

        return max_area           