class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        # Log(m * n) = Log(m) + Log(n)
        start_row, end_row = 0, len(matrix) - 1
        while start_row <= end_row:
            mid_row = (start_row + end_row) // 2
            if matrix[mid_row][0] < target and matrix[mid_row][-1] > target:
                break
            if matrix[mid_row][0] > target:
                end_row = mid_row - 1
            else:
                start_row = mid_row + 1

        row = (start_row + end_row) // 2
        start_col, end_col = 0, len(matrix[row]) - 1
        while start_col <= end_col:
            mid_col = (start_col + end_col) // 2
            if matrix[row][mid_col] == target:
                return True
            if matrix[row][mid_col] > target:
                end_col = mid_col - 1
            else:
                start_col = mid_col + 1

        return False


if __name__ == "__main__":
    f = Solution().searchMatrix
    print(f([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))  # True
    print(f([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13))  # False
    print(f([[1]], 2))  # False
