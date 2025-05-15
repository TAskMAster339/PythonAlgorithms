from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree1(
        self,
        preorder: list[int],
        inorder: list[int],
    ) -> Optional[TreeNode]:
        return self.build1(preorder, inorder)

    def build(
        self,
        preorder: list[int],
        inorder: list[int],
    ) -> Optional[TreeNode]:
        if inorder:
            indx = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[indx])

            root.left = self.build(preorder, inorder[:indx])
            root.right = self.build(preorder, inorder[indx + 1 :])

            return root

        return None

    def buildTree2(
        self,
        preorder: list[int],
        inorder: list[int],
    ) -> Optional[TreeNode]:
        mapping = {}

        for i in range(len(inorder)):
            mapping[inorder[i]] = i

        def build(start: int, end: int) -> Optional[TreeNode]:
            if start > end:
                return None

            mid = mapping[preorder.pop(0)]
            root = TreeNode(inorder[mid])

            root.left = build(start, mid - 1)
            root.right = build(mid + 1, end)

            return root

        return build(0, len(preorder) - 1)
