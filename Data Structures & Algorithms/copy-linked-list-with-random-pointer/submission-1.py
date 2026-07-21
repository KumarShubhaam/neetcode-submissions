"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        lookup = {}
        curr = head
        while curr:
            copy_node = Node(curr.val, None, None)
            lookup[curr] = copy_node
            curr = curr.next

        curr = head
        while curr:
            copy_node = lookup[curr]
            copy_node.next = lookup.get(curr.next)
            copy_node.random = lookup.get(curr.random)
            curr = curr.next

        return lookup.get(head)
        