class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def binary_search(is_left: bool):
            start, end, indx = 0, len(nums) - 1, -1

            while start <= end:
                mid = (start + end) // 2
                if nums[mid] < target:
                    start = mid + 1
                elif nums[mid] > target:
                    end = mid - 1
                else:
                    indx = mid
                    if is_left:
                        end = mid - 1
                    else:
                        start = mid + 1

            return indx

        left = binary_search(is_left=True)
        right = binary_search(is_left=False)
        return [left, right]


if __name__ == "__main__":
    f = Solution().searchRange
    print(f([5, 7, 7, 8, 8, 10], 8))  # [3, 4]
    print(f([5, 7, 7, 8, 8, 10], 6))  # [-1, -1]
    print(f([], 0))  # [-1, -1]
