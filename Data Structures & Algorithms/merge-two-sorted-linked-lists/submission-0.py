class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        prev = dummy
        curr = list1
        curr_ = list2 

        while curr and curr_:
            if curr.val < curr_.val:
                prev.next = curr
                curr = curr.next
            else: 
                prev.next = curr_
                curr_ = curr_.next
            prev = prev.next

        prev.next = curr if curr else curr_
        return dummy.next