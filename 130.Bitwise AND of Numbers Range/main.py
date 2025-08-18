class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        num = 0
        while left < right:
            left >>= 1
            right >>= 1
            num += 1
        return left << num


if __name__ == "__main__":
    f = Solution().rangeBitwiseAnd
    print(f(5, 7))  # 4
    print(f(0, 0))  # 0
    print(f(0, 2147483647))  # 0
