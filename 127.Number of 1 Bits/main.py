class Solution:
    def hammingWeight(self, n: int) -> int:
        result = 0
        while n:
            result += n & 1
            n >>= 1
        return result


if __name__ == "__main__":
    f = Solution().hammingWeight
    print(f(11))  # 3
    print(f(128))  # 1
    print(f(2147483645))  # 30
