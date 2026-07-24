# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def helper(self, root):
        if root is None:
            return 0, 0 # max

        left, max_l = self.helper(root.left)
        right, max_r = self.helper(root.right)
        
        max_d = max(left+right, max_l, max_r)

        return max(left, right)+1, max_d

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_depth, max_d = self.helper(root)
        return max(max_depth-1, max_d)

                