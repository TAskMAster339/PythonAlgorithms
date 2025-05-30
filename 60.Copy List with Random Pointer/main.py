from typing import Optional


class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if not head:
            return None

        # Copy of all Nodes
        curr = head
        while curr:
            new_node = Node(curr.val, curr.next)
            curr.next = new_node
            curr = new_node.next

        curr = head
        # make new Random nodes connections
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        old_head = head
        new_head = head.next
        curr_old = old_head
        curr_new = new_head

        # Slice two lists
        while curr_old:
            curr_old.next = curr_old.next.next
            curr_new.next = curr_new.next.next if curr_new.next else None
            curr_old = curr_old.next
            curr_new = curr_new.next

        return new_head
