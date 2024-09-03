class Solution:
    def detectCycle(self, head):
        """
        head: Optional[ListNode]) -> Optional[ListNode]
        """
        fast = head
        slow = head

        while fast is not None:
            slow = slow.next
            fast = fast.next
            if fast is None:
                break
            else:
                fast = fast.next

            if fast == slow:
                slow = head
                while fast != slow:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None
