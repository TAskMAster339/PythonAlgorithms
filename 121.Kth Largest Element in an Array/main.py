import heapq


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heapq._heapify_max(nums)
        result = -1

        for _ in range(k):
            result = heapq._heappop_max(nums)
        return result


if __name__ == "__main__":
    f = Solution().findKthLargest
    print(f([3, 2, 1, 5, 6, 4], 2))  # 5
    print(f([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))  # 4
