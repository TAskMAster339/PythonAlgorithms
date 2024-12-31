from typing import List
from util import test_case


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        table = {}
        result = 0
        for num in nums:
            left = table.get(num - 1, 0)
            right = table.get(num + 1, 0)
            length = left + right + 1
            table[num - left] = length
            table[num + right] = length
            result = max(result, length)
        return result


if __name__ == "__main__":
    f = Solution().longestConsecutive
    test_case(f, 4, nums=[100, 4, 200, 1, 3, 2])
    test_case(f, 9, nums=[0, 3, 7, 2, 5, 8, 4, 6, 0, 1])
