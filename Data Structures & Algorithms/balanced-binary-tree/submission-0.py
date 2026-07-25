# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def helper(self, root):
        if root is None:
            return True, 0

        isLeft, left = self.helper(root.left)
        isRight, right = self.helper(root.right)

        if not isLeft or not isRight:
            return False, max(left, right) + 1

        if abs(right - left) > 1:
            return False, max(left, right) + 1

        return True, max(left, right) + 1


    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        isBalanced, height = self.helper(root)
        return isBalanced
        