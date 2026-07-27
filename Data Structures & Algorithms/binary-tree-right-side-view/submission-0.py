# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        res = []

        q = collections.deque()
        q.append(root)
        while q:
            length = len(q)
            level = None
            for i in range(length):
                curr = q.popleft()
                if level is None:
                    level = curr.val
                if curr.right:
                    q.append(curr.right)
                if curr.left:
                    q.append(curr.left)
            res.append(level)

        return res
        