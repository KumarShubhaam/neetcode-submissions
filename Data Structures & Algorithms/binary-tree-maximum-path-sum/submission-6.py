# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def helper(root):
            if root.left is None and root.right is None:
                print('None', root.val, 'None')
                return root.val, root.val

            # s = root.val
            s = max_seen = root.val
            left = right = None
            if root.left:
                left, left_max = helper(root.left)
            if root.right:
                right, right_max = helper(root.right)

            if left and right:
                print(left, root.val, right)
                s = max(left+root.val, root.val+right, root.val)
                max_seen = max(left_max, right_max, left+root.val+right, s)
            elif left:
                print(left, root.val, 'None')
                s = max(left+root.val, root.val)
                max_seen = max(left_max, root.val+left, s)
            elif right:
                print('None', root.val, right)
                s = max(right+root.val, root.val)
                max_seen = max(right_max, root.val+right, s)
            print('s =',s, 'max_seen =', max_seen)
            return s, max_seen

        return max(helper(root))

