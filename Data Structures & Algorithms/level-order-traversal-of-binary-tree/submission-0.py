# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        res = []
        queue = collections.deque()
        queue.append(root)
        queue.append(None)
        child = []
        while queue:
            curr = queue.popleft()
            if curr is None:
                res.append(child)
                if queue:
                    queue.append(None)
                child = []
            else:
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                child.append(curr.val)
            # print(curr.val, res) if curr else print('None', res)

        return res


