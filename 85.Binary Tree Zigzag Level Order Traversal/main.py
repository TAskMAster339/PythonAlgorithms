from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        if not root:
            return []
        result = []

        queue = [root]

        right_to_left_flag = False

        while queue:
            size = len(queue)
            level = [0] * size

            for i in range(len(queue)):
                node = queue.pop(0)
                if node:
                    index = size - 1 - i if right_to_left_flag else i
                    level[index] = node.val
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            result.append(level)
            right_to_left_flag = not right_to_left_flag
        return result
