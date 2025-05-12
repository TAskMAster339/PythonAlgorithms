from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(
        self, head: Optional[ListNode], k: int
    ) -> Optional[ListNode]:
        end = head
        length = 1
        if not end or not end.next:
            return head

        while end.next:
            end = end.next
            length += 1

        k %= length

        if k == 0:
            return head

        start = head
        prev = None

        for i in range(length - k):
            prev = start
            start = start.next

        prev.next = None
        end.next = head
        return start
