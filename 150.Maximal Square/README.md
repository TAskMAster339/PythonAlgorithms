<div align='center'>
<h1><a href='https://leetcode.com/problems/maximal-square/description/'><strong>150) Maximal Square</strong></a></h1>
</div>

## **Условие:**

Дана двоичная матрица **matrix** размером **m** **x** **n**, в ней только **0** и **1**. Необходимо найти наибольший квадрат, который состоит из **1**. Необходимо вернуть его площадь

## **Идея:**

Динамически рассчитывать квадратик

## **Реализация:**

Создадим матрицу **dp**, где в **dp**[**i**][**j**] будет записана сторона наибольшего квадрата, правым нижнем углом которого является клетка [**i**][**j**].

Будем динамически итерироваться по матрице **matrix**. Если **matrix**[**i**][**j**] == "**1**", то мы обновляем **dp**[**i**][**j**] = **min**(**dp**[**i**][**j** - **1**], **dp**[**i** - **1**][**j**], **dp**[**i** - **1**][**j** - **1**]) + **1**. Так как по умолчанию матрица **dp** заполнена **0**, то **min**(...) будет равняться не **0**, если **4** смежных клетки не равны **0**. (Смотри картинку).

Таким образом мы динамически будем вычислять длину стороны наибольшего квадрата единичек. В конце нужно вернуть площадь этого квадрата.



## **Оценка:**

По времени сложность будет (**N** * **M**), где **n** **x** **m** - размер матрица **matrix**.

Сложность по памяти будет **O**(**N** * **M**), размеры матрицы **dp**.

## Код:
```python
class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        dp = [[0] * len(matrix[i]) for i in range(len(matrix))]

        max_square_side = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == "1":
                    left = dp[i][j - 1] if j > 0 else 0
                    top = dp[i - 1][j] if i > 0 else 0
                    diag = dp[i - 1][j - 1] if i > 0 and j > 0 else 0
                    dp[i][j] = min(left, top, diag) + 1
                    max_square_side = max(max_square_side, dp[i][j])

        for row in dp:
            print(row)

        return max_square_side**2


if __name__ == "__main__":
    f = Solution().maximalSquare
    print(
        f(
            [
                ["1", "0", "1", "0", "0"],
                ["1", "0", "1", "1", "1"],
                ["1", "1", "1", "1", "1"],
                ["1", "0", "0", "1", "0"],
            ],
        ),
    )  # 4
    print(
        f(
            [
                ["0", "1"],
                ["1", "0"],
            ],
        ),
    )  # 1

```

<div align='center'><h3><a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/149.Best%20Time%20to%20Buy%20and%20Sell%20Stock%20IV'>⬅️ предыдущая задача</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/README.md'>Все задачи</a></h3></div>