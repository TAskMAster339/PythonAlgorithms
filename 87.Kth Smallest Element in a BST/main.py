from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        smallest = 0

        def dfs(node: Optional[TreeNode]) -> None:
            nonlocal smallest, k
            if k < 0:
                return
            if node:
                dfs(node.left)

                k -= 1
                if k == 0:
                    smallest = node.val

                dfs(node.right)

        dfs(root)
        return smallest
