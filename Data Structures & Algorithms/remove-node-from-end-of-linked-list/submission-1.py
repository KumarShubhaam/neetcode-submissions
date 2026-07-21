# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        f = head
        for i in range(n):
            f = f.next

        b = dummy
        while f:
            f = f.next
            b = b.next

        b.next = b.next.next
        return dummy.next
