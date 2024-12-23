from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][j] = '0'

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '0':
                    matrix[i][j] = 0
                    for ii in range(len(matrix)):
                        if matrix[ii][j] != '0':
                            matrix[ii][j] = 0
                    for jj in range(len(matrix[0])):
                        if matrix[i][jj] != '0':
                            matrix[i][jj] = 0


if __name__ == "__main__":
    s = Solution()
    mat1 = [[1, 1, 1],
            [1, 0, 1],
            [1, 1, 1]]
    s.setZeroes(mat1)
    print(mat1)
    mat2 = [[0, 1, 2, 0],
            [3, 4, 5, 2],
            [1, 3, 1, 5]]
    s.setZeroes(mat2)
    print(mat2)
