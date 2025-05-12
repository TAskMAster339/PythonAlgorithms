from typing import List
from util import test_case


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows, columns = len(matrix), len(matrix[0])
        x, y, dx, dy = 0, 0, 1, 0
        result = []

        for k in range(rows * columns):
            result.append(matrix[y][x])
            matrix[y][x] = "*"

            if (
                not 0 <= x + dx < columns
                or not 0 <= y + dy < rows
                or matrix[y + dy][x + dx] == "*"
            ):
                dx, dy = -dy, dx

            x += dx
            y += dy

        return result


if __name__ == "__main__":
    s = Solution()
    test_case(
        s.spiralOrder,
        [1, 2, 3, 6, 9, 8, 7, 4, 5],
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    )
    test_case(
        s.spiralOrder,
        [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7],
        [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
    )
