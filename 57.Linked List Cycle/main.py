from typing import Optional
from util import test_case


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True

        return False


if __name__ == "__main__":
    start = ListNode(3)
    second = ListNode(2)
    third = ListNode(0)
    fourth = ListNode(5)
    last = ListNode(-4)
    start.next = second
    second.next = third
    third.next = fourth
    fourth.next = last
    last.next = second

    uno_lst = ListNode(1)
    f = Solution().hasCycle
    test_case(f, True, start)
    test_case(f, False, uno_lst)