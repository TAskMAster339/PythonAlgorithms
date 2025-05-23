from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        path_sum = 0

        def dfs(root: Optional[TreeNode]) -> int:
            nonlocal path_sum

            if not root:
                return 0

            left_sum = max(0, dfs(root.left))
            right_sum = max(0, dfs(root.right))

            path_sum = max(path_sum, left_sum + right_sum + root.val)

            return root.val + max(left_sum, right_sum)

        dfs(root)
        return path_sum
