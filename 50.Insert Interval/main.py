from typing import List
from util import test_case


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i = 0

        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
            i += 1
        result.append(newInterval)

        while i < len(intervals):
            result.append(intervals[i])
            i += 1

        return result


if __name__ == "__main__":
    f = Solution().insert
    test_case(f, [[1, 5], [6, 9]], intervals=[[1, 3], [6, 9]], newInterval=[2, 5])
    test_case(f, [[1, 2], [3, 10], [12, 16]], intervals=[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], newInterval=[4, 8])
    test_case(f, [[1, 7]], [[1, 5]], [2, 7])
