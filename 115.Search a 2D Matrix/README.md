<div align='center'>
<h1><a href='https://leetcode.com/problems/search-a-2d-matrix/description/'><strong>115) Search a 2D Matrix</strong></a></h1>
</div>

## **Условие:**

Дана матрица целых чисел **matrix** размером **M** **x** **N** с следующими особенностями. Каждая строка отсортирована в неубывающем порядке. Первое число каждой строки больше последнего числа предыдущей.

Дано число **target**. Нужно вернуть **True**, если оно есть в матрице, иначе **False**.

Необходимо сделать это за **O**(**log**(**N** * **M**))

## **Идея:**

Бинарный поиск в матрице. А еще если вспомнить, что **log**(**N** * **M**) = **log**(**N**) + **log**(**M**), то понятно, что это просто два последовательных бинарных поиска

## **Реализация:**

Сделаем сначала бинарный поиск строки, в которой может быть наше число. Из условия мы можем понять, что мы можем с помощью последнего или первого числа в строке определить искомый ряд.

После этого тем же бинарным поиском ищем наше число в найденной строке. Если нашли, возвращаем **True**. Иначе **False**.



## **Оценка:**

По времени два бинарных поиска займут **O**(**log**(**M** * **N**)), где **M** - количество строк в матрице, **N** - количество столбцов.

По памяти мы затратим **O**(**1**), так не создаем какие-либо вспомогательные структуры данных.

## Код:
```python
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

```

<div align='center'><h3><a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/114.Search%20Insert%20Position'>⬅️ предыдущая задача</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/README.md'>Все задачи</a></h3></div>