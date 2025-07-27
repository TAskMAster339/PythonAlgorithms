class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        summary = 0
        result = nums[0]
        for num in nums:
            summary = max(num, summary + num)
            result = max(result, summary)

        return result


if __name__ == "__main__":
    f = Solution().maxSubArray
    print(f([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
    print(f([1]))  # 1
    print(f([5, 4, -1, 7, 8]))  # 23
