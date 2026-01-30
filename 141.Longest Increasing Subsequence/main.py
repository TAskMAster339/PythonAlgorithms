class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        dp = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

    def lengthOfLIS_BS(self, nums: list[int]) -> int:
        lis = []

        def binary_search(arr: list[int], target: int) -> int:
            start, end = 0, len(arr) - 1
            while start <= end:
                mid = (start + end) // 2
                if arr[mid] == target:
                    return mid
                if arr[mid] > target:
                    end = mid - 1
                else:
                    start = mid + 1
            return start

        for num in nums:
            if not lis or lis[-1] < num:
                lis.append(num)
            else:
                idx = binary_search(lis, num)
                lis[idx] = num
        return len(lis)


if __name__ == "__main__":
    f = Solution().lengthOfLIS_BS
    print(f([10, 9, 2, 5, 3, 7, 101, 18]))  # 4
    print(f([0, 1, 0, 3, 2, 3]))  # 4
    print(f([7, 7, 7, 7, 7, 7, 7]))  # 1
    print(f([4, 10, 4, 3, 8, 9]))  # 3
