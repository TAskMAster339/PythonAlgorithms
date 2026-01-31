class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0

        dp = [[0] * len(obstacleGrid[i]) for i in range(len(obstacleGrid))]

        dp[0][0] = 1
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[i])):
                if i == j == 0:
                    continue
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                    continue

                top = dp[i - 1][j] if i - 1 >= 0 else 0
                left = dp[i][j - 1] if j - 1 >= 0 else 0
                dp[i][j] = top + left

        return dp[-1][-1]


if __name__ == "__main__":
    f = Solution().uniquePathsWithObstacles
    print(f([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))  # 2
    print(f([[0, 1], [0, 0]]))  # 1
