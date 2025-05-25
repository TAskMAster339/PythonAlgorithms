<div align='center'>
<h1><a href='https://leetcode.com/problems/valid-sudoku/description/'><strong>34) Valid Sudoku</strong></a></h1>
</div>

## **Условие:**

Дана матрица **9x9**, которая представляет собой судоку. Нужно проверить удовлетворяет ли она правилам судоку:

**1**) Каждый слой должен содержать цифры от **1** до **9** без повторений

**2**) Каждый столбец должен содержать цифры от **1** до **9** без повторений

**3**) Каждый из девяти **3x3** под-судоку должен содержать цифры от **1** до **9** без повторений

Символ "." используется для обозначение пустого места, его проверять не нужно.

## **Идея:**

Проверить все правила судоку.

## **Реализация:**

Первое мое решение сделано через **3** функции, каждая из которой проходит по матрице и проверяет отведенное ей условие, затем с помощь логического "И" мы объединяем их результаты и возвращаем.

Но более интересно сделать это за один проход по матрице. Для этого придется задействовать дополнительную память. Создадим для каждого столбца, каждой строки, каждого кубика свое множество.

Теперь проходя по матрице мы будем проверять: находится ли **board**[**i**][**j**] элемент в **rows**[**i**], или в **columns**[**j**], или в **cubes**[**cube_index**] (Индекс куба вычисляем по следующий формуле **3** * (**i** // **3**) + **j** // **3**).

Если элемент находится в хотя бы одном множестве возвращаем **False**, иначе добавляем этот элемент в эти три множества, продолжаем цикл.

В конце возвращаем **True**



## **Оценка:**

По времени мы потратим **O**(**1**), хотя на самом деле это будет **O**(**N**^**2**), так как перебор всех элементов матрицы стоит **N**^**2** действий, но по правилам судоку матрица будет константного размера **9**^**2**, следовательно **O**(**81**) = **O**(**1**), по памяти мы потратим тоже **O**(**1**) (Здесь то же самое, если бы матрица не была бы **9x9**, то мы бы затратили **O**(**3** * **N**^**2**) = **O**(**N**^**2**) (**3** массива, где в массиве **N** множеств, а в множестве **N** элементов)).

Еще внизу я прикреплю время работы двух решений. Их асимптотическое время одинаковое, оба по **O**(**1**), но фактическое время работы отличается. Нашли закономерность?

## Код:
```python
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

```

<div align='center'><h3><a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/33.Minimum%20Window%20Substring'>⬅️ предыдущая задача</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/README.md'>Все задачи</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/35.Spiral%20Matrix'>следующая задача ➡️</a></h3></div>