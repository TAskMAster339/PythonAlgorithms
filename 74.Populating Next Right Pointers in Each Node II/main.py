class Node:
    def __init__(
        self,
        val: int = 0,
        left: "Node" = None,
        right: "Node" = None,
        next: "Node" = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: "Node") -> "Node":
        queue = [(root, 0)]
        prev_node = (None, 0)

        while queue:
            node, level = queue.pop(0)
            if node:
                if prev_node[1] == level:
                    node.next = prev_node[0]
                prev_node = (node, level)
                queue.append((node.right, level + 1))
                queue.append((node.left, level + 1))

    def connect2(self, root: "Node") -> "Node":
        if not root:
            return None

        curr = root
        dummy = Node(-999)
        head = root

        while head:
            curr = head  # initialize current level's head
            prev = dummy  # init prev for next level linked list traversal
            # iterate through the linked-list of the current level and
            # connect all the siblings in the next level
            while curr:
                if curr.left:
                    prev.next = curr.left
                    prev = prev.next
                if curr.right:
                    prev.next = curr.right
                    prev = prev.next
                curr = curr.next
            head = dummy.next  # update head to the linked list of next level
            dummy.next = None  # reset dummy node
        return root
