from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less = ListNode()
        more = ListNode()

        start = less
        end = more

        while head:
            if head.val < x:
                less.next = ListNode(head.val)
                less = less.next
            else:
                more.next = ListNode(head.val)
                more = more.next
            head = head.next

        less.next = end.next
        return start.next
