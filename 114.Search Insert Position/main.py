class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        def binarySearch(start: int, end: int) -> int:
            if start > end:
                return start

            mid = (start + end) // 2

            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                return binarySearch(start, mid - 1)
            return binarySearch(mid + 1, end)

        return binarySearch(0, len(nums) - 1)


if __name__ == "__main__":
    f = Solution().searchInsert
    print(f([1, 3, 5, 6], 5))
    print(f([1, 3, 5, 6], 2))
    print(f([1, 3, 5, 6], 7))
