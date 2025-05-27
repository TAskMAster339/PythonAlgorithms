from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        min_diff = float("inf")
        prev_node = None

        def dfs(node: Optional[TreeNode]) -> None:
            nonlocal min_diff, prev_node
            if node:
                dfs(node.left)
                if prev_node:
                    min_diff = min(min_diff, node.val - prev_node.val)
                prev_node = node
                dfs(node.right)

        dfs(root)
        return min_diff
