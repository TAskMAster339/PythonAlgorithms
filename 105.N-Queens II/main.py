class Solution:
    def totalNQueens(self, n: int) -> int:
        QUEEN = "Q"
        DOT = "."
        board = [[DOT] * n for i in range(n)]

        def check_queen_pos(row: int, column: int) -> bool:
            for r in range(n):
                if board[r][column] == QUEEN:
                    return False
            for c in range(n):
                if board[row][c] == QUEEN:
                    return False
            r, c = row - 1, column - 1
            while r >= 0 and c >= 0:
                if board[r][c] == QUEEN:
                    return False
                r -= 1
                c -= 1
            r, c = row - 1, column + 1
            while r >= 0 and c < n:
                if board[r][c] == QUEEN:
                    return False
                r -= 1
                c += 1
            return True

        def backtrack(row: int) -> int:
            if row == n:
                return 1
            count = 0
            for col in range(n):
                if check_queen_pos(row, col):
                    board[row][col] = QUEEN
                    count += backtrack(row + 1)
                    board[row][col] = DOT
            return count

        return backtrack(0)


if __name__ == "__main__":
    f = Solution().totalNQueens
    print(f(4))  # 2
    print(f(1))  # 1
    print(f(8))  # 92
