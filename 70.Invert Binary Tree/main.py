from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        tmp_node = root.left
        root.left = root.right
        root.right = tmp_node

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
