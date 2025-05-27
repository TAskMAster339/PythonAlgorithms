from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        flag = True
        prev_node = None

        def dfs(node: Optional[TreeNode]) -> None:
            nonlocal flag, prev_node

            if not flag:
                return
            if node:
                dfs(node.left)
                if prev_node:
                    flag = prev_node.val > node.val
                prev_node = node
                dfs(node.right)

        dfs(root)
        return flag
