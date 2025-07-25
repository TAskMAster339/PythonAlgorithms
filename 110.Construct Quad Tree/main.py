class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: list[list[int]]) -> Node:
        if len(grid) == 1:
            return Node(grid[0][0], True, None, None, None, None)
        n = len(grid) // 2
        topLeft = self.construct([row[:n] for row in grid[:n]])
        topRight = self.construct([row[n:] for row in grid[:n]])
        bottomLeft = self.construct([row[:n] for row in grid[n:]])
        bottomRight = self.construct([row[n:] for row in grid[n:]])
        if (topLeft.val == topRight.val == bottomLeft.val == bottomRight.val) and (
            topLeft.isLeaf
            and topRight.isLeaf
            and bottomLeft.isLeaf
            and bottomRight.isLeaf
        ):
            return Node(topLeft.val, isLeaf=True)
        return Node(1, False, topLeft, topRight, bottomLeft, bottomRight)


if __name__ == "__main__":
    X = [
        [1, 1, 0, 0],
        [0, 0, 1, 1],
        [1, 1, 0, 0],
        [0, 0, 1, 1],
    ]
    Y = [[1, 1], [0, 0]]
    n = len(Y) // 2
    print([row[:n] for row in Y[:n]])
    print([row[n:] for row in Y[:n]])
    print([row[:n] for row in Y[n:]])
    print([row[n:] for row in Y[n:]])
