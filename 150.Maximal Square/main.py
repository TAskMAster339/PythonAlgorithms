class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        dp = [[0] * len(matrix[i]) for i in range(len(matrix))]

        max_square_side = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == "1":
                    left = dp[i][j - 1] if j > 0 else 0
                    top = dp[i - 1][j] if i > 0 else 0
                    diag = dp[i - 1][j - 1] if i > 0 and j > 0 else 0
                    dp[i][j] = min(left, top, diag) + 1
                    max_square_side = max(max_square_side, dp[i][j])

        for row in dp:
            print(row)

        return max_square_side**2


if __name__ == "__main__":
    f = Solution().maximalSquare
    print(
        f(
            [
                ["1", "0", "1", "0", "0"],
                ["1", "0", "1", "1", "1"],
                ["1", "1", "1", "1", "1"],
                ["1", "0", "0", "1", "0"],
            ],
        ),
    )  # 4
    print(
        f(
            [
                ["0", "1"],
                ["1", "0"],
            ],
        ),
    )  # 1
