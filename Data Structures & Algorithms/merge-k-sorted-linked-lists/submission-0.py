# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummyHead = ListNode(0)
        dummy = dummyHead
        dummyTail = ListNode(float('inf'))

        min_node = dummyTail
        while dummy:
            min_node = dummyTail
            index = len(lists)
            for i, ll in enumerate(lists):
                if ll and ll.val < min_node.val:
                    # print(ll.val)
                    min_node = ll
                    index = i
            if dummy and index < len(lists):
                dummy.next = min_node
                lists[index] = lists[index].next
                dummy = dummy.next
            else:
                break

        return dummyHead.next

                        