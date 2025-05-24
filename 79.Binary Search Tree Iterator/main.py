from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.stack = []

    def next(self) -> int:
        while self.root:
            self.stack.append(self.root)
            self.root = self.root.left
        nxt = self.stack.pop()
        self.root = nxt.right
        return nxt.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0 or self.root is not None
