class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[amount] if dp[amount] != float("inf") else -1


if __name__ == "__main__":
    f = Solution().coinChange
    print(f([1, 2, 5], 11))  # 3
    print(f([2], 3))  # -1
    print(f([1], 0))  # 0
    print(f([186, 419, 83, 408], 6249))  # 20
