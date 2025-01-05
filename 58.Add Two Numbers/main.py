from typing import Optional
from util import test_case


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        returnList = ListNode(0)
        begin = returnList
        carry = 0

        while l1 or l2 or carry != 0:
            digit1 = l1.val if l1 else 0
            digit2 = l2.val if l2 else 0

            total = (digit1 + digit2 + carry) % 10
            carry = (digit1 + digit2 + carry) // 10

            newNode = ListNode(total)
            returnList.next = newNode
            returnList = returnList.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        result = begin.next
        begin.next = None
        begin = None
        return result


if __name__ == "__main__":
    first = ListNode(2)
    first2 = ListNode(4)
    first3 = ListNode(3)
    first.next = first2
    first2.next = first3

    second = ListNode(5)
    second2 = ListNode(6)
    second3 = ListNode(4)
    second.next = second2
    second2.next = second3

    f = Solution().addTwoNumbers(first, second)

    while f:
        print(f.val)
        f = f.next
