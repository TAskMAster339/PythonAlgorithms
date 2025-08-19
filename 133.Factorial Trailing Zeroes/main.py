class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        while n:
            count += n // 5
            n //= 5
        return count


if __name__ == "__main__":
    f = Solution().trailingZeroes
    print(f(3))  # 0
    print(f(5))  # 1
    print(f(0))  # 0
    print(f(25))  # 5
    print(f(127))  # 31
