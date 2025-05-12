from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        newList = ListNode(0)
        begin = newList

        while list1 or list2:
            val1 = list1.val if list1 else float("inf")
            val2 = list2.val if list2 else float("inf")

            if val1 < val2:
                newList.next = ListNode(val1)
                list1 = list1.next if list1 else None
            elif val2 <= val1:
                newList.next = ListNode(val2)
                list2 = list2.next if list2 else None
            newList = newList.next

        result = begin.next
        begin.next = None
        begin = None
        return result


if __name__ == "__main__":
    list1 = ListNode(1, ListNode(2, ListNode(4)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))

    f = Solution().mergeTwoLists(list1, list2)
    while f:
        print(f.val)
        f = f.next
