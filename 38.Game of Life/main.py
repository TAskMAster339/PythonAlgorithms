from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        zero_sign = "*"
        one_sign = "$"

        for i in range(len(board)):
            for j in range(len(board[i])):
                count_one = 0
                for di in range(-1, 2):
                    for dj in range(-1, 2):
                        if -1 < i + di < len(board) and -1 < j + dj < len(
                            board[i]
                        ):
                            if di == 0 and dj == 0:
                                continue
                            if (
                                board[i + di][j + dj] == 1
                                or board[i + di][j + dj] == zero_sign
                            ):
                                count_one += 1

                if board[i][j] == 1:
                    if count_one < 2 or count_one > 3:
                        board[i][j] = zero_sign
                        continue
                if board[i][j] == 0:
                    if count_one == 3:
                        board[i][j] = one_sign
                        continue

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == zero_sign:
                    board[i][j] = 0
                if board[i][j] == one_sign:
                    board[i][j] = 1


if __name__ == "__main__":
    s = Solution()
    board1 = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
    s.gameOfLife(board1)
    Output1 = [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]
    print(board1)
    board2 = [[1, 1], [1, 0]]
    s.gameOfLife(board2)
    Output2 = [[1, 1], [1, 1]]
    print(board2)
