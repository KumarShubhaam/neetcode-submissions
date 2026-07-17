class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if not nums1:
            n = len(nums2)
            mid = (n // 2)
            if n % 2 == 0:
                median = (nums2[mid-1] + nums2[mid]) / 2
            else:
                median = nums2[mid]*2/2
            return median

        if not nums2:
            n = len(nums1)
            mid = (n // 2)
            if n % 2 == 0:
                median = (nums1[mid-1] + nums1[mid]) / 2
            else:
                median = nums1[mid]*2/2
            return median

        n = len(nums1) + len(nums2)
        mid = (n-1) // 2

        x, y = 0, 0
        while x + y < n:
            if x + y == mid:
                if n % 2 == 0:
                    median = (nums1[x] + nums2[y])/2
                else:
                    median = ((min(nums1[x], nums2[y])) * 2) / 2
                return median
            if nums1[x] < nums2[y]:
                x += 1
            else:
                y += 1

        
         