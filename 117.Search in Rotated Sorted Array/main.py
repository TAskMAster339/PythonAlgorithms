class Solution:
    def search(self, nums: list[int], target: int) -> int:
        start, end = 0, len(nums) - 1

        while start <= end:
            mid = (start + end) // 2

            if nums[mid] == target:
                return mid
            if nums[start] <= nums[mid]:
                if nums[start] <= target <= nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if nums[mid] <= target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1


if __name__ == "__main__":
    f = Solution().search
    print(f([4, 5, 6, 7, 0, 1, 2], 0))  # 4
    print(f([4, 5, 6, 7, 0, 1, 2], 3))  # -1
    print(f([1], 0))  # -1
    print(f([1, 3], 0))  # -1
    print(f([3, 1], 1))  # 1
    print(f([5, 1, 3], 1))  # 1
