from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        start = 0
        result = set()
        for i in range(1, len(height)):
            if height[i] >= height[start]:
                result.add((start, i))
                start = i
        end = len(height) - 1
        for i in range(len(height) - 2, -1, -1):
            if height[i] >= height[end]:
                result.add((i, end))
                end = i
        water = 0
        for pair in result:
            min_height = min(height[pair[0]], height[pair[1]])
            for i in range(pair[0] + 1, pair[1]):
                water += min_height - height[i]
        return water

    def trap2(self, height: List[int]) -> int:
        start = 0
        result = 0
        tmp = 0
        for i in range(1, len(height)):
            small = height[start]
            tmp += (small - height[i]) if (small - height[i]) > 0 else 0
            if height[i] >= height[start]:
                result += tmp
                start = i
                tmp = 0
        end = len(height) - 1
        tmp = 0
        for i in range(len(height) - 2, -1, -1):
            small = height[end]
            tmp += (small - height[i]) if (small - height[i]) > 0 else 0
            if height[i] > height[end]:
                result += tmp
                end = i
                tmp = 0
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))  # 6
    print(s.trap([4, 2, 0, 3, 2, 5]))  # 9
