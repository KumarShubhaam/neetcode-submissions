# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(inorder) == 0:
            return None

        root = preorder[0]
        for i,n in enumerate(inorder):
            if n == root:
                break

        # print('left', root, preorder[1:], inorder[:i])
        left_node = self.buildTree(preorder[1:], inorder[:i])

        # print('right', root, preorder[2:] if left_node else preorder[1:], inorder[i+1:])
        # print('right', root, preorder[len(inorder[:i])+1:], inorder[i+1:])
        # right_node = self.buildTree(preorder[2:] if left_node else preorder[1:], inorder[i+1:])
        right_node = self.buildTree(preorder[len(inorder[:i])+1:], inorder[i+1:])

        root_node = TreeNode(root, left_node, right_node)
        # print('root_node=', root_node.val)

        return root_node
        