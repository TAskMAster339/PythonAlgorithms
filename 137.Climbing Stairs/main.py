class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n

        dp = [0] * (n + 1)
        dp[1], dp[2] = 1, 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]


if __name__ == "__main__":
    f = Solution().climbStairs
    print(f(2))  # 2
    print(f(3))  # 3
