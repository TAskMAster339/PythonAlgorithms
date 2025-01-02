from typing import List
from util import test_case


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        table = dict()

        for i in range(len(nums)):
            if nums[i] in table:
                if i - table[nums[i]] <= k:
                    return True
            table[nums[i]] = i
        return False


if __name__ == "__main__":
    f = Solution().containsNearbyDuplicate
    test_case(f, True, nums=[1, 2, 3, 1], k=3)
    test_case(f, True, nums=[1, 0, 1, 1], k=1)
    test_case(f, False, [1, 2, 3, 1, 2, 3], k=2)
