from typing import List
from util import timer


class Solution:
    @timer
    def isValidSudoku2(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        cubes = [set() for _ in range(9)]

        for row in range(9):
            for column in range(9):
                item = board[row][column]

                if item == ".":
                    continue

                cube_index = 3 * (row // 3) + column // 3
                if (
                    item in rows[row]
                    or item in columns[column]
                    or item in cubes[cube_index]
                ):
                    return False

                rows[row].add(item)
                columns[column].add(item)
                cubes[cube_index].add(item)

        return True

    @timer
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return (
            self.vertical_check(board)
            and self.horizontal_check(board)
            and self.cube_check(board)
        )

    def vertical_check(self, board: List[List[str]]) -> bool:
        num_count = [0] * 10
        for i in range(len(board)):
            line = board[i]
            for item in line:
                if item == ".":
                    continue
                num_count[int(item)] += 1
            if any(elem > 1 for elem in num_count):
                return False
            else:
                num_count = [0] * 10
        return True

    def horizontal_check(self, board: List[List[str]]) -> bool:
        num_count = [0] * 10
        for i in range(9):
            for line in board:
                item = line[i]
                if item == ".":
                    continue
                num_count[int(item)] += 1

            if any(elem > 1 for elem in num_count):
                return False
            else:
                num_count = [0] * 10
        return True

    def cube_check(self, board: List[List[str]]) -> bool:
        num_count = [0] * 10

        for i in range(0, len(board), 3):
            count = 0
            for line in board:
                item1 = line[i]
                item2 = line[i + 1]
                item3 = line[i + 2]
                count += 3
                if item1.isnumeric():
                    num_count[int(item1)] += 1
                if item2.isnumeric():
                    num_count[int(item2)] += 1
                if item3.isnumeric():
                    num_count[int(item3)] += 1
                if count == 9:
                    if any(elem > 1 for elem in num_count):
                        return False
                    else:
                        num_count = [0] * 10
                        count = 0
        return True


if __name__ == "__main__":
    s = Solution()
    print("First example")
    print(
        s.isValidSudoku(
            [
                ["5", "3", ".", ".", "7", ".", ".", ".", "."],
                ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                [".", "9", "8", ".", ".", ".", ".", "6", "."],
                ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                [".", "6", ".", ".", ".", ".", "2", "8", "."],
                [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                [".", ".", ".", ".", "8", ".", ".", "7", "9"],
            ]
        )
    )  # True
    print(
        s.isValidSudoku2(
            [
                ["5", "3", ".", ".", "7", ".", ".", ".", "."],
                ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                [".", "9", "8", ".", ".", ".", ".", "6", "."],
                ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                [".", "6", ".", ".", ".", ".", "2", "8", "."],
                [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                [".", ".", ".", ".", "8", ".", ".", "7", "9"],
            ]
        )
    )  # True
    print("\nSecond example")
    print(
        s.isValidSudoku(
            [
                ["8", "3", ".", ".", "7", ".", ".", ".", "."],
                ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                [".", "9", "8", ".", ".", ".", ".", "6", "."],
                ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                [".", "6", ".", ".", ".", ".", "2", "8", "."],
                [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                [".", ".", ".", ".", "8", ".", ".", "7", "9"],
            ]
        )
    )  # False
    print(
        s.isValidSudoku2(
            [
                ["8", "3", ".", ".", "7", ".", ".", ".", "."],
                ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                [".", "9", "8", ".", ".", ".", ".", "6", "."],
                ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                [".", "6", ".", ".", ".", ".", "2", "8", "."],
                [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                [".", ".", ".", ".", "8", ".", ".", "7", "9"],
            ]
        )
    )  # False
