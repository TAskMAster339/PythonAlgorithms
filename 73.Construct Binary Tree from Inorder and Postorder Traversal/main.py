from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(
        self,
        inorder: list[int],
        postorder: list[int],
    ) -> Optional[TreeNode]:
        table = {}

        for i in range(len(inorder)):
            table[inorder[i]] = i

        def build(start: int, end: int) -> Optional[TreeNode]:
            if start > end:
                return None
            root_value = postorder.pop()
            root = TreeNode(root_value)

            middle_index = table[root_value]
            root.right = build(middle_index + 1, end)
            root.left = build(start, middle_index - 1)

            return root

        return build(0, len(postorder) - 1)
