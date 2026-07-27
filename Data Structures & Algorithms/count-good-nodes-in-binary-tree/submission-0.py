# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def helper(root, up_bound):
            if root is None:
                return 0
            
            if root.val >= up_bound:
                count = 1
            else:
                count = 0
            
            up_bound = max(up_bound, root.val)
            left = helper(root.left, up_bound)
            right = helper(root.right, up_bound)

            return left + right + count

        return helper(root, float('-inf'))

        