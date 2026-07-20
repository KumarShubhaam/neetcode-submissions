# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find the mid
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow
        slow = mid.next
        mid.next = None
        # print('mid', mid.val)

        # find the tail
        tail = None
        while slow:
            nxt = slow.next
            slow.next = tail
            tail = slow
            slow = nxt
        # print('tail', tail.val)

        curr = head
        while tail:
            temp = tail
            tail = tail.next

            nxt = curr.next
            curr.next = temp
            temp.next = nxt
            curr = nxt
