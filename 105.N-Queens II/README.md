<div align='center'>
<h1><a href='https://leetcode.com/problems/n-queens-ii/description/'><strong>105) N-Queens II</strong></a></h1>
</div>

## **Условие:**

Проблема **N** ферзей - это проблема расстановки **N** ферзей на шахматной доске **N** **x** **N** таким образом, чтобы ни один ферзь не атаковал другого.

Необходимо вернуть количество уникальных решений проблемы **N** ферзей

## **Идея:**

Решить задачу **N** ферзей и посчитать количество решений

## **Реализация:**

Сначала надо создать доску размером **N** **x** **N**, заполним её ".", ферзя будем обозначать "**Q**".

Мы будем перебирать все варианты, для этого создадим рекурсивную функцию **backtrack**, которая будет принимать строку **row** и итерироваться по столбцам **col**.

Крайний случай - **row** == **n**, мы дошли до конца доски, в этом случае возвращаем **1**.

В рекуррентном случае создаем переменную **count** = **0**. И начинаем итерироваться по столбцам. Мы будем пытаться поставить в [**row**][**col**] клетку на доске ферзя, если это возможно. (Проверка нет ли ферзя на этой строке, в этом столбце, на двух диагоналях, можно оптимизировать так как мы двигаемся слева направо, сверху вниз, то есть нам нет смысла проверять правую часть диагонали, но это никак не повлияет на асимптотику скорости)

Если ферзя можно поставить, то мы его ставим и вызываем **backtrack**(**row** + **1**) и записываем результат вызова в **count**, затем не забываем сделать возврат. В конце возвращаем **count**.

В конце внешней функции мы вызываем и возвращаем **backtrack**(**0**).



## **Оценка:**

Сложность по времени будет **O**(**N**! * **N**), так как каждый ферзь в наихудшем случае будет уменьшать количество вариантов на **1**. Получим **N** * (**N** - **1**) * (**N** - **2**) * ... При этом мы каждый раз проверяем валидность возможности поставить ферзя, что будет **O**(**N**).

Сложность по памяти будет **O**(**N**^**2**), так как нам необходимо хранить доску размером **N** * **N**.

## Код:
```python
class Solution:
    def totalNQueens(self, n: int) -> int:
        QUEEN = "Q"
        DOT = "."
        board = [[DOT] * n for i in range(n)]

        def check_queen_pos(row: int, column: int) -> bool:
            for r in range(n):
                if board[r][column] == QUEEN:
                    return False
            for c in range(n):
                if board[row][c] == QUEEN:
                    return False
            r, c = row - 1, column - 1
            while r >= 0 and c >= 0:
                if board[r][c] == QUEEN:
                    return False
                r -= 1
                c -= 1
            r, c = row - 1, column + 1
            while r >= 0 and c < n:
                if board[r][c] == QUEEN:
                    return False
                r -= 1
                c += 1
            return True

        def backtrack(row: int) -> int:
            if row == n:
                return 1
            count = 0
            for col in range(n):
                if check_queen_pos(row, col):
                    board[row][col] = QUEEN
                    count += backtrack(row + 1)
                    board[row][col] = DOT
            return count

        return backtrack(0)


if __name__ == "__main__":
    f = Solution().totalNQueens
    print(f(4))  # 2
    print(f(1))  # 1
    print(f(8))  # 92

```

<div align='center'><h3><a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/104.Combination%20Sum'>⬅️ предыдущая задача</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/README.md'>Все задачи</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/106.Generate%20Parentheses'>следующая задача ➡️</a></h3></div>