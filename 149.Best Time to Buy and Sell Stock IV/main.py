class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:
        n = len(prices)
        dp = [[[0] * 2 for _ in range(k + 1)] for _ in range(n)]

        for j in range(1, k + 1):
            dp[0][j][1] = -prices[0]

        for i in range(1, n):
            for j in range(1, k + 1):
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i])
                dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i])

        return dp[n - 1][k][0]


if __name__ == "__main__":
    f = Solution().maxProfit
    print(f(2, [2, 4, 1]))  # 2
    print(f(2, [3, 2, 6, 5, 0, 3]))  # 7
