from typing import Optional

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return None
        table = {node.val: Node(node.val)}
        queue = [node]
        while queue:
            curr_node = queue.pop(0)
            curr_node_copy = table[curr_node.val]
            neighbors = []
            for n in curr_node.neighbors:
                if n.val not in table:
                    table[n.val] = Node(n.val)
                    queue.append(n)
                neighbors.append(table[n.val])
            curr_node_copy.neighbors = neighbors

        return table[node.val]
