from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for row in range(len(matrix)):
            for column in range(row, len(matrix[row])):
                matrix[row][column], matrix[column][row] = matrix[column][row], matrix[row][column]
        for row in matrix:
            row.reverse()


if __name__ == "__main__":
    s = Solution()
    mat1 = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]

    s.rotate(mat1)
    print(mat1)
    mat2 = [[5, 1, 9, 11],
            [2, 4, 8, 10],
            [13, 3, 6, 7],
            [15, 14, 12, 16]]
    s.rotate(mat2)
    print(mat2)
