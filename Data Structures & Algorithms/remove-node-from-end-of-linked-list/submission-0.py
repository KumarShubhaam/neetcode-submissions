# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        f = head
        for i in range(n):
            f = f.next

        if f is None:
            return head.next
        
        b = head
        while f.next:
            f = f.next
            b = b.next

        if f == b:
            return None

        b.next = b.next.next
        return head
        

        