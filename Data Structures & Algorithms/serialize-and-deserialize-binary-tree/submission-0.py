# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # N,2,N, 1, N,3,N,5,N
        if root is None:
            return ''

        def bfs(root):
            q = collections.deque()
            q.append(root)
            res = ''
            while q:
                length = len(q)
                for i in range(length):
                    curr = q.popleft()
                    if curr:
                        res += f'{curr.val}'
                        q.append(curr.left)
                        q.append(curr.right)
                    else:
                        res += 'N'
                    res += ','
            return res[:-1]

    
        return bfs(root)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # ['1', '2', '3', 'N', 'N', '4', '5', 'N', 'N', 'N', 'N']

        bfs_arr = data.split(',')
        # if len(bfs_arr) == 0:
        #     print(len(bfs_arr))
        #     return None

        print(bfs_arr, len(bfs_arr))
        q = collections.deque()
        head = TreeNode(bfs_arr[0])
        q.append(head)
        i = 1
        while q and i < len(bfs_arr):
            curr = q.popleft()

            if bfs_arr[i] != 'N':
                left = TreeNode(bfs_arr[i])
                q.append(left)
                curr.left = left
            i += 1

            if bfs_arr[i] != 'N':
                right = TreeNode(bfs_arr[i])
                q.append(right)
                curr.right = right
            i += 1
            
        return head

