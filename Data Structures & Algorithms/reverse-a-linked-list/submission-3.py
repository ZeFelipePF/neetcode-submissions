# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: empty list or last node
        if head is None or head.next is None:
            return head

        # Recurse all the way to the end first
        new_head = self.reverseList(head.next)

        # Now do the actual reversal on the way back
        head.next.next = head   # make the next node point back to me
        head.next = None        # break my old forward pointer

        return new_head