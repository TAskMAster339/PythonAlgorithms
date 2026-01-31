class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        dp = [[float("inf")] * len(grid[i]) for i in range(len(grid))]
        dp[0][0] = grid[0][0]

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if i + 1 < len(grid):
                    dp[i + 1][j] = min(dp[i + 1][j], grid[i + 1][j] + dp[i][j])
                if j + 1 < len(grid[i]):
                    dp[i][j + 1] = min(dp[i][j + 1], grid[i][j + 1] + dp[i][j])
        return dp[-1][-1]


if __name__ == "__main__":
    f = Solution().minPathSum
    print(f([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))  # 7
    print(f([[1, 2, 3], [4, 5, 6]]))  # 12
