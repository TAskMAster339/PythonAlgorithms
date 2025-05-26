from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        result = []

        queue = [root]

        while queue:
            level = []

            for _ in range(len(queue)):
                node = queue.pop(0)
                if node:
                    level.append(node)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)

            result.append(level)
        return result
