from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        if not head and left == right:
            return head

        result = ListNode(0, head)
        LeftPointer, current = result, head

        for i in range(left - 1):
            LeftPointer, current = current, current.next

        prevPointer = None
        for i in range(right - left + 1):
            nextNodePointer = current.next
            current.next = prevPointer
            prevPointer, current = current, nextNodePointer

        LeftPointer.next.next = current
        LeftPointer.next = prevPointer
        return result.next
