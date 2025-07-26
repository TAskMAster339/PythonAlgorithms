from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        n = len(lists) // 2
        left = self.mergeKLists(lists[:n])
        right = self.mergeKLists(lists[n:])
        return self.merge2Lists(left, right)

    def merge2Lists(self, first: ListNode, second: ListNode) -> ListNode:
        dummy = ListNode()
        cur = dummy
        while first and second:
            if first.val < second.val:
                cur.next = first
                first = first.next
            else:
                cur.next = second
                second = second.next
            cur = cur.next

        if first:
            cur.next = first
        if second:
            cur.next = second

        return dummy.next
