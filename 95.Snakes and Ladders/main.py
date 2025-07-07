from collections import deque


class Solution:
    def snakesAndLadders(self, board: list[list[int]]) -> int:
        n = len(board)
        target = n**2
        dist = [-1] * (target + 1)
        start = 1
        dist[start] = 0
        queue = deque([start])

        while queue:
            current = queue.popleft()
            for i in range(1, 7):
                next = current + i
                if next > target:
                    break

                row = (next - 1) // n
                col = (next - 1) % n
                value = board[n - 1 - row][(n - 1 - col) if (row % 2 == 1) else col]
                move = value if value > 0 else next

                if move == target:
                    return dist[current] + 1

                if dist[move] == -1:
                    dist[move] = dist[current] + 1
                    queue.append(move)
        return -1


if __name__ == "__main__":
    f = Solution().snakesAndLadders
    print(
        f(  # 4
            [
                [-1, -1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1, -1],
                [-1, 35, -1, -1, 13, -1],
                [-1, -1, -1, -1, -1, -1],
                [-1, 15, -1, -1, -1, -1],
            ],
        ),
    )
    print(f([[-1, -1], [-1, 3]]))  # 1
