# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(root):
            if root is None:
                return True, float('inf'), float('-inf')

            left, left_min, left_max = helper(root.left)
            right, right_min, right_max = helper(root.right)

            curr_min = min(left_min, right_min, root.val)
            curr_max = max(left_max, right_max, root.val)

            if not left or not right:
                return False, curr_min, curr_max

            if root.val <= left_max or root.val >= right_min:
                return False, curr_min, curr_max

            return True, curr_min, curr_max

        return helper(root)[0]


        