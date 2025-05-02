from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start = head
        if not start or start.next is None:
            return head

        left = start
        right = start.next
        prev = None

        while True:
            if left.val != right.val:
                prev = left
                left = right
                right = right.next
            else:
                while right and left.val == right.val:
                    right = right.next
                if prev:
                    prev.next = right
                    left = prev
                else:
                    left = right
                    if right:
                        right = right.next
                    start = left
            if not right:
                break
        return start
