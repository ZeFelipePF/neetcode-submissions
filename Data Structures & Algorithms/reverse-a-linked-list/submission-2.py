# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        else:
            prev, middle, nextt = head, head.next, head.next.next

        while middle: 
            middle.next = prev
            prev = middle
            middle = nextt
            if nextt is not None:
                nextt = nextt.next
            head.next = None
        return prev