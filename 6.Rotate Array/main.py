from typing import List


def invert(nums, start, end):
    for i in range(start, (start+end) // 2):
        nums[i], nums[end - 1] = nums[end - 1], nums[i]
        end -= 1


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k %= len(nums)
        invert(nums, 0, len(nums))
        invert(nums, 0, k)
        invert(nums, k, len(nums))


if __name__ == "__main__":
    s = Solution()
    s.rotate([1,2,3,4,5,6,7], 3)
    s.rotate([-1,-100,3,99], 2)
