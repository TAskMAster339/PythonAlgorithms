<div align='center'>
<h1><a href='https://leetcode.com/problems/unique-paths-ii/description/'><strong>144) Unique Paths II</strong></a></h1>
</div>

## **Условие:**

Дана матрица целых чисел **m** **x** **n** **grid**. Есть робот, расположенный в левом верхнем углу, ему необходимо добраться до правого нижнего угла. Робот может двигаться только вниз или вправо. В ячейках **grid** могут быть числа **0** и **1**, **0** - свободное место, на которое может пойти робот. **1** - препятствие, на которое не может пойти робот.

Необходимо посчитать количество уникальных путей доступных роботу.

## **Идея:**

Практически идентичная предыдущей задачи задача

## **Реализация:**

Создаем матрицу **dp**, где в **dp**[**i**][**j**] будет записано количество способов добрать до этой ячейки. Оно будет вычисляться динамически как сумма **dp**[**i** - **1**][**j**] и **dp**[**i**][**j** - **1**], единственных доступных ходов. Также стоит не забывать не считать пути, где есть камушки.

Остается не корректно обработать крайний случай, где **grid**[**0**][**0**] либо равна **1**, если там не камень, иначе **0**.

В конце получаем ответ в ячейки **dp**[-**1**][-**1**].



## **Оценка:**

По времени сложность алгоритма - **O**(**N** * **M**), где **N** * **M** - размерность матрицы.

По памяти сложность алгоритма - **O**(**N** * **M**).

## Код:
```python
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0

        dp = [[0] * len(obstacleGrid[i]) for i in range(len(obstacleGrid))]

        dp[0][0] = 1
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[i])):
                if i == j == 0:
                    continue
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                    continue

                top = dp[i - 1][j] if i - 1 >= 0 else 0
                left = dp[i][j - 1] if j - 1 >= 0 else 0
                dp[i][j] = top + left

        return dp[-1][-1]


if __name__ == "__main__":
    f = Solution().uniquePathsWithObstacles
    print(f([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))  # 2
    print(f([[0, 1], [0, 0]]))  # 1

```

<div align='center'><h3><a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/143.Minimum%20Path%20Sum'>⬅️ предыдущая задача</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/README.md'>Все задачи</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/145.Longest%20Palindromic%20Substring'>следующая задача ➡️</a></h3></div>