from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        result = []

        queue = [root]

        while queue:
            right_side_view = None

            for _ in range(len(queue)):
                node = queue.pop(0)
                if node:
                    right_side_view = node
                    queue.append(node.left)
                    queue.append(node.right)
            if right_side_view:
                result.append(right_side_view.val)
        return result
