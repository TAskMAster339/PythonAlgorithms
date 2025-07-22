class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        def backtrack(i: int, j: int, word_idx: int) -> bool:
            if word_idx == len(word):
                return True

            if (
                i < 0
                or i >= len(board)
                or j < 0
                or j >= len(board[0])
                or board[i][j] != word[word_idx]
            ):
                return False

            temp = board[i][j]
            board[i][j] = ""

            if (
                backtrack(i + 1, j, word_idx + 1)
                or backtrack(i - 1, j, word_idx + 1)
                or backtrack(i, j + 1, word_idx + 1)
                or backtrack(i, j - 1, word_idx + 1)
            ):
                return True

            board[i][j] = temp
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i, j, 0):
                    return True

        return False


if __name__ == "__main__":
    f = Solution().exist
    print(
        f([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"),
    )
    print(f([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE"))
    print(f([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB"))
