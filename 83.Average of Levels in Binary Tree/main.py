from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> list[float]:
        result = []

        queue = [root]

        while queue:
            sum_of_level = 0
            num = len(queue)

            for _ in range(len(queue)):
                node = queue.pop(0)
                if node:
                    sum_of_level += node.val
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            result.append(sum_of_level / num)
        return result
