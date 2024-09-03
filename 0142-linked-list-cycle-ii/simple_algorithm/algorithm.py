class Solution:
    def detectCycle(self, head):
        """
        head: Optional[ListNode]) -> Optional[ListNode]
        """
        visited = dict()
        cur = head
        pos = 0
        while cur != None:
            if cur.next in visited:
                return cur.next
            visited[cur] = pos
            pos += 1
            cur = cur.next
        return None
