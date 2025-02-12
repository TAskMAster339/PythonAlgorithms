from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast_pointer = head

        for i in range(n):
            fast_pointer = fast_pointer.next

        if not fast_pointer:
            return head.next

        slow_pointer = head
        prev = None

        while fast_pointer:
            fast_pointer = fast_pointer.next
            prev = slow_pointer
            slow_pointer = slow_pointer.next

        prev.next = prev.next.next

        return head
