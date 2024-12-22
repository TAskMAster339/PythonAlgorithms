from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        cur_sum = nums[left]
        min_len = float('inf')

        while right != len(nums) - 1 or left != len(nums):
            if cur_sum >= target:
                min_len = min(min_len, right - left + 1)
                cur_sum -= nums[left]
                left += 1
                continue
            else:
                right += 1
                if right >= len(nums):
                    return min_len if min_len != float('inf') else 0
            cur_sum += nums[right]
        return min_len if min_len != float('inf') else 0


if __name__ == "__main__":
    s = Solution()
    print(s.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
    print(s.minSubArrayLen(4, [1, 4, 4]))
    print(s.minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]))
    print(s.minSubArrayLen(11, [1, 2, 3, 4, 5]))  # 3
    print(s.minSubArrayLen(7, [1, 1, 1, 1, 7]))
