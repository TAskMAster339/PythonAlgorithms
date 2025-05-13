from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return self.maxDepthRecursive(root, 1)

    def maxDepthRecursive(self, node: Optional[TreeNode], depth: int) -> int:
        if not node:
            return depth

        if not node.left and not node.right:
            return depth

        leftSubTreeDepth = self.maxDepthRecursive(node.left, depth + 1)
        rightSubTreeDepth = self.maxDepthRecursive(node.right, depth + 1)

        return max(leftSubTreeDepth, rightSubTreeDepth)
