class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        prefix = [0] * length
        suffix = [0] * length

        temp = 0
        for i,n in enumerate(height):
            prefix[i] = temp
            temp = max(temp, n)
        # print('prefix', prefix)

        temp = 0
        for i in range(length-1, -1, -1):
            suffix[i] = temp
            temp = max(temp, height[i])
            # print(height[i])
        # print('suffix', suffix)

        max_water = 0
        for i in range(length):
            min_h = min(prefix[i], suffix[i])
            water = min_h - height[i]
            if water > 0:
                max_water += water

        return max_water