from typing import List
from util import test_case


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        result = []
        left = 0
        right = 1
        while left != right:
            if right < len(nums) and nums[right] - nums[right - 1] > 1:
                if nums[left] == nums[right - 1]:
                    string = f"{nums[left]}"
                else:
                    string = f"{nums[left]}->{nums[right - 1]}"
                result.append(string)
                left = right
            if right <= len(nums) - 1:
                right += 1
            else:
                if nums[left] == nums[right - 1]:
                    string = f"{nums[left]}"
                else:
                    string = f"{nums[left]}->{nums[right - 1]}"
                result.append(string)
                left = right
        return result


if __name__ == "__main__":
    f = Solution().summaryRanges
    test_case(f, ["0->2", "4->5", "7"], [0, 1, 2, 4, 5, 7])
    test_case(f, ["0", "2->4", "6", "8->9"], [0, 2, 3, 4, 6, 8, 9])
