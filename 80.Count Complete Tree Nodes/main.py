from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left_depth = self.get_depth(root.left, is_left=True)
        right_depth = self.get_depth(root.right, is_left=False)

        if left_depth == right_depth:
            return (1 << left_depth) - 1  # <=> 2**left_depth - 1

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    def get_depth(
        self,
        node: Optional[TreeNode],
        *,
        is_left: bool = True,
    ) -> int:
        depth = 1
        while node:
            node = node.left if is_left else node.right
            depth += 1
        return depth
