# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        arr = []
        if head is None:
            index = -1
            return False
        else:
            while head.next:
                if head in arr:
                    index = arr.index(head)
                    return True
                else:
                    arr.append(head)
                    head = head.next
            index = -1
            return False

        