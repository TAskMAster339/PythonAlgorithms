from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        near = far = jumps = 0

        while far < len(nums) - 1:
            farthest = 0
            for i in range(near, far + 1):
                farthest = max(farthest, i + nums[i])

            near = far + 1
            far = farthest
            jumps += 1

        return jumps

    def jump2(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0  # Already at the last index

        jumps = 0
        current_end = 0
        farthest = 0

        for i in range(n - 1):  # No need to check the last element
            # Update the farthest point reachable from here
            jump = i + nums[i]
            if farthest < jump:
                farthest = jump

            # If we have reached the end of the current jump's range
            if i == current_end:
                jumps += 1
                current_end = farthest

                # If the current_end reaches or goes beyond the last index
                if current_end > n - 1:
                    break

        return jumps


if __name__ == "__main__":
    s = Solution()
    print(s.jump2([2, 3, 1, 1, 4]))
    print(s.jump2([2, 3, 0, 1, 4]))
    print(s.jump([1, 2]))
    print(s.jump([1, 2, 3]))
    print(s.jump([0]))
    print(s.jump([1, 2, 1, 1, 1]))  # 3
