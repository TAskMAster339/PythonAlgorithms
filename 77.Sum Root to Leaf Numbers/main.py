from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, 0)

    def dfs(self, root: Optional[TreeNode], num: int) -> int:
        if not root:
            return 0

        num = 10 * num + root.val
        if not root.left and not root.right:
            return num
        return self.dfs(root.left, num) + self.dfs(root.right, num)
