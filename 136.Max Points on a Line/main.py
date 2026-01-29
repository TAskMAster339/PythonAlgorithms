from collections import defaultdict


class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        if len(points) <= 2:
            return len(points)

        def slope(p1, p2):
            if p1[0] == p2[0]:
                return float("inf")
            return (p2[1] - p1[1]) / (p2[0] - p1[0])

        ans = 1

        for i, p1 in enumerate(points):
            slopes = defaultdict(int)
            for _, p2 in enumerate(points[i + 1 :]):
                slp = slope(p1, p2)
                slopes[slp] += 1
                ans = max(ans, slopes[slp])
        return ans + 1


if __name__ == "__main__":
    f = Solution().maxPoints
    print(f([[1, 1], [2, 2], [3, 3]]))  # 3
    print(f([[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]))  # 4
