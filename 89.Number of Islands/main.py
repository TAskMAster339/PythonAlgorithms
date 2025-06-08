class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        visited = set()
        m = len(grid)
        n = len(grid[0])

        def dfs(x, y):
            queue = [(x, y)]

            while queue:
                point_x, point_y = queue.pop(0)
                if (point_x, point_y) in visited:
                    continue
                visited.add((point_x, point_y))
                if point_x + 1 < m and grid[point_x + 1][point_y] == "1":
                    queue.append((point_x + 1, point_y))
                if point_y + 1 < n and grid[point_x][point_y + 1] == "1":
                    queue.append((point_x, point_y + 1))
                if point_x - 1 >= 0 and grid[point_x - 1][point_y] == "1":
                    queue.append((point_x - 1, point_y))
                if point_y - 1 >= 0 and grid[point_x][point_y - 1] == "1":
                    queue.append((point_x, point_y - 1))

        count = 0

        for j in range(n):
            for i in range(m):
                if grid[i][j] == "1" and (i, j) not in visited:
                    dfs(i, j)
                    count += 1

        return count




if __name__ == "__main__":
    s = Solution()
    print(s.numIslands(
        [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"],
        ],
    ))
    print(s.numIslands(
        [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"],
        ],
    ))
    print(s.numIslands(
        [
        ["1","1","1"],
        ["0","1","0"],
        ["1","1","1"],
        ],
    ))
