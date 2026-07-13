class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        index = -1
        while l <= r:
            mid = l + ((r-l)//2)
            if target >=  matrix[mid][0] and target <= matrix[mid][-1]:
                index = mid
                break
            elif target > matrix[mid][-1]:
                l = mid + 1
            else:
                r = mid - 1
            

        print('row:', matrix[index])

        x, y = 0, len(matrix[index]) - 1
        while x <= y:
            mid = x + ((y-x)//2)
            if matrix[index][mid] < target:
                x = mid + 1
            elif matrix[index][mid] > target:
                y = mid - 1
            else:
                return True

        return False

