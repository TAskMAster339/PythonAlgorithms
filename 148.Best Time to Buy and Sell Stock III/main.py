class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy1 = buy2 = float("inf")
        profit1 = profit2 = 0

        for price in prices:
            buy1 = min(buy1, price)
            profit1 = max(profit1, price - buy1)

            buy2 = min(buy2, price - profit1)
            profit2 = max(profit2, price - buy2)

        return profit2


if __name__ == "__main__":
    f = Solution().maxProfit
    print(f([3, 3, 5, 0, 0, 3, 1, 4]))  # 6
    print(f([1, 2, 3, 4, 5]))  # 4
    print(f([7, 6, 4, 3, 1]))  # 0
