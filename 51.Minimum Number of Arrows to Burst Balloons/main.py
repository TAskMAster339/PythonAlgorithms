from typing import List
from util import test_case


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points.sort(key=lambda x: x[1])

        union = []
        start = points[0][0]
        end = points[0][1]
        for x, y in points[1:]:
            if end < x:
                union.append([start, end])
                start = 0
                end = float("inf")
            start = max(start, x)
            end = min(end, y)
        union.append([start, end])

        return len(union)

    def findMinArrowShots2(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points.sort(key=lambda x: x[1])
        prev = points[0]
        total = 1
        for i in points[1:]:
            if prev[1] < i[0]:
                prev = i
                total += 1
        return total


if __name__ == "__main__":
    f = Solution().findMinArrowShots2
    test_case(f, 2, points=[[10, 16], [2, 8], [1, 6], [7, 12]])
    test_case(f, 4, [[1, 2], [3, 4], [5, 6], [7, 8]])
    test_case(f, 2, points=[[1, 2], [2, 3], [3, 4], [4, 5]])
    test_case(f, 0, [])
    test_case(f, 2, [[1, 2], [4, 5], [1, 5]])
    test_case(f, 2, [[3, 9], [7, 12], [3, 8], [6, 8], [9, 10], [2, 9], [0, 9], [3, 9], [0, 6], [2, 8]])
