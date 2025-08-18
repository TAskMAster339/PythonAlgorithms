class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        ones = 0
        twos = 0
        for num in nums:
            ones ^= num & ~twos
            twos ^= num & ~ones
        return ones


if __name__ == "__main__":
    f = Solution().singleNumber
    print(f([2, 2, 3, 2]))  # 3
    print(f([0, 1, 0, 1, 0, 1, 99]))  # 99
