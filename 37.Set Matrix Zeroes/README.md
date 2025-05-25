<div align='center'>
<h1><a href='https://leetcode.com/problems/set-matrix-zeroes/description/'><strong>37) Set Matrix Zeroes</strong></a></h1>
</div>

## **Условие:**

Дана матрица целых чисел размером **m** на **n**, если элемент равен нулю, нужно сделать ряд и колонку, в которых находится этот элемент, нулевыми. Сделать это нужно на месте.

## **Идея:**

Когда мы будем обнулять строки и столбцы на месте, мы обнулим всю матрицу, если не запомним какие нули были изначально в матрице, а какие были нами добавлены.

## **Реализация:**

Сделаем этот алгоритм в два прохода.

В первом проходе мы заменим все нули на "*".

Во втором проходе мы будем искать эти звездочки и выполнять то, что требует от нас условие задачи.



## **Оценка:**

По времени мы затратим **O**(**N** * **M**) (В наихудшем случае придется отметить **N** * **M** нулей и заменить их **N** * **M** действий), по памяти мы затратим **O**(**1**).

## Код:
```python
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][j] = "0"

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "0":
                    matrix[i][j] = 0
                    for ii in range(len(matrix)):
                        if matrix[ii][j] != "0":
                            matrix[ii][j] = 0
                    for jj in range(len(matrix[0])):
                        if matrix[i][jj] != "0":
                            matrix[i][jj] = 0


if __name__ == "__main__":
    s = Solution()
    mat1 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    s.setZeroes(mat1)
    print(mat1)
    mat2 = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    s.setZeroes(mat2)
    print(mat2)

```

<div align='center'><h3><a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/36.Rotate%20Image'>⬅️ предыдущая задача</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/README.md'>Все задачи</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/38.Game%20of%20Life'>следующая задача ➡️</a></h3></div>