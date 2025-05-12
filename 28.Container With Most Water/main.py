from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        left, right = 0, len(height) - 1
        while left < right:
            maxArea = max(
                maxArea, min(height[left], height[right]) * (right - left)
            )
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxArea


if __name__ == "__main__":
    s = Solution()
    print(s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
    print(s.maxArea([1, 1]))
