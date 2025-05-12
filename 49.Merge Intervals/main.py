from typing import List
from util import test_case


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:  # so bad
        intervals.sort(key=lambda arr: arr[0])
        left = 0
        right = 1
        while right < len(intervals):
            first = intervals[left]
            second = intervals[right]
            if second[0] <= first[1]:
                newLine = [first[0], max(second[1], first[1])]
                intervals.pop(right)
                intervals[left] = newLine
            else:
                left += 1
                right += 1
        return intervals

    def merge2(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i: i[0])
        output = [intervals[0]]

        for start, end in intervals[1:]:
            lastEnd = output[-1][1]
            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])
        return output


if __name__ == "__main__":
    f = Solution().merge
    test_case(
        f, [[1, 6], [8, 10], [15, 18]], [[1, 3], [2, 6], [8, 10], [15, 18]]
    )
    test_case(f, [[1, 5]], [[1, 4], [4, 5]])
    test_case(f, [[1, 3]], [[1, 3]])
    test_case(f, [[1, 4], [5, 6]], [[1, 4], [5, 6]])
    test_case(f, [[0, 5]], [[1, 4], [0, 2], [3, 5]])
