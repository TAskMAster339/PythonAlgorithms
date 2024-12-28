from typing import List
from util import test_case


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = dict()
        for i in range(len(nums)):
            table[nums[i]] = i

        for i in range(len(nums)):
            pair_element = target - nums[i]
            if pair_element in table and table[pair_element] != i:
                return [i, table[pair_element]]


if __name__ == "__main__":
    f = Solution().twoSum
    test_case(f, [0, 1], nums=[2, 7, 11, 15], target=9)
    test_case(f, [1, 2], nums=[3, 2, 4], target=6)
    test_case(f, [0, 1], nums=[3, 3], target=6)
