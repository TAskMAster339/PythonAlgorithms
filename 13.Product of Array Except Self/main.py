from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums)
        prefix[0] = nums[0]
        suffix = [0] * len(nums)
        suffix[-1] = nums[-1]

        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i]

        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i]

        result = [0] * len(nums)
        for i in range(len(nums)):
            if i + 1 == len(nums):
                result[i] = prefix[i - 1]
            elif i == 0:
                result[i] = suffix[i + 1]
            else:
                result[i] = suffix[i + 1] * prefix[i - 1]
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.productExceptSelf([1, 2, 3, 4]))
    print(s.productExceptSelf([-1, 1, 0, -3, 3]))
