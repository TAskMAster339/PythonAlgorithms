class Solution:
    def findMin(self, nums: list[int]) -> int:
        start, end = 0, len(nums) - 1

        while start < end:
            mid = (start + end) // 2
            if nums[mid] > nums[end]:
                start = mid + 1
            else:
                end = mid
        return nums[start]


if __name__ == "__main__":
    f = Solution().findMin
    print(f([3, 4, 5, 1, 2]))  # 1
    print(f([4, 5, 6, 7, 0, 1, 2]))  # 0
    print(f([11, 13, 15, 17]))  # 11
