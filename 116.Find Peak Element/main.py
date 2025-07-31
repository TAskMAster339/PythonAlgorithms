class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return 0

        start, end = 0, len(nums) - 1

        while start <= end:
            mid = (start + end) // 2
            if (
                (mid == 0 and nums[mid + 1] < nums[mid])
                or (mid == len(nums) - 1 and nums[mid - 1] < nums[mid])
            ) or (nums[mid - 1] < nums[mid] and nums[mid + 1] < nums[mid]):
                return mid
            if nums[mid + 1] > nums[mid]:
                start = mid + 1
            elif nums[mid - 1] > nums[mid]:
                end = mid - 1
        return start


if __name__ == "__main__":
    f = Solution().findPeakElement
    print(f([1, 2, 3, 1]))  # 2
    print(f([1, 2, 1, 3, 5, 6, 4]))  # 5
