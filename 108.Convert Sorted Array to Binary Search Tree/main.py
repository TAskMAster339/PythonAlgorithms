from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> Optional[TreeNode]:
        def convert(left, right) -> TreeNode:
            if left > right:
                return None
            mid = (left + right) // 2

            root = TreeNode(nums[mid])

            root.left = convert(left, mid - 1)
            root.right = convert(mid + 1, right)

            return root

        return convert(0, len(nums) - 1)
