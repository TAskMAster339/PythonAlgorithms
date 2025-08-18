class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result


if __name__ == "__main__":
    f = Solution().singleNumber
    print(f([2, 2, 1]))  # 1
    print(f([4, 1, 2, 1, 2]))  # 4
    print(f([1]))  # 1
