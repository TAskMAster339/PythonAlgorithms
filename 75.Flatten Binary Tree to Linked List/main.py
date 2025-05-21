from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        left_node = root

        while left_node:
            if left_node.left:
                right_subtree = left_node.right
                left_node.right = left_node.left
                left_node.left = None
                left_node = left_node.right  # next left node

                join_node = left_node
                while join_node and join_node.right:
                    join_node = join_node.right

                join_node.right = right_subtree
            elif left_node.right:
                left_node = left_node.right
            else:
                break

        return root
