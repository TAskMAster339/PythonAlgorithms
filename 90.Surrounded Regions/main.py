class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        queue = []

        for i in range(m):
            if board[i][0] == "O":
                queue.append((i, 0))
            if board[i][n - 1] == "O":
                queue.append((i, n - 1))

        for j in range(n):
            if board[0][j] == "O":
                queue.append((0, j))
            if board[m - 1][j] == "O":
                queue.append((m - 1, j))

        while queue:
            cur_r, cur_c = queue.pop(0)
            board[cur_r][cur_c] = "*"
            for dr, dc in directions:
                new_r = cur_r + dr
                new_c = cur_c + dc
                if 0 <= new_r < m and 0 <= new_c < n and board[new_r][new_c] == "O":
                    queue.append((new_r, new_c))

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "*":
                    board[i][j] = "O"



if __name__ == "__main__":
    s = Solution()
    target = [
            ["X","X","X","X"],
            ["X","O","O","X"],
            ["X","X","O","X"],
            ["X","O","X","X"],
        ]
    s.solve(target)

    for row in target:
        print(row)

