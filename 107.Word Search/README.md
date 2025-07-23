<div align='center'>
<h1><a href='https://leetcode.com/problems/word-search/description/'><strong>107) Word Search</strong></a></h1>
</div>

## **Условие:**

Дана доска **board** размером **m** **x** **n** и строка **word**, нужно вернуть **True**, если слово можно составить на доске.

Слово, составленное на доске, - это слово, которое получено соединением соседних ячеек по горизонтали или по вертикали. При этом каждая ячейка используется ровно один раз

## **Идея:**

Уже была такая задача под номером **100**), но мы попытаемся оптимизировать его

## **Реализация:**

Для этого создадим вспомогательную функцию **backtrack**.

Крайний случай состоит из двух частей: **1**) Когда глубина рекурсии стала равна длине слова. То есть если мы спустились так глубоко, то мы нашли слово, возвращаем **True**. **2**) Если мы получили нету букву или некорректный индекс, то в этом случае мы возвращаем **False**.

Рекуррентный случай состоит из вызовов функции **backtrack** для клеток сверху, снизу, слева, справа. Если хотя бы один из ник возвращает истину, то мы вернем **True**. (Это можно понять так, мы ищем слово **Tree**, мы его нашли, если начали с буквы **T** и рядом с ней найдено слово **ree** и так далее рекурсивно)

При этом **backtrack** заключается в том, что мы будем на время спуска заменять значение **board**[**i**][**j**] == "", при этом не забываем сохранять это значение, чтобы после окончания была возможность совершить откат.

Осталось пройти по всем клеткам доски и вызвать для каждой нашу функцию. Если хотя бы один вызов вернет **True**, возвращаем **True**, иначе в конце возвращаем **False**.



## **Оценка:**

Сложность по времени будет **O**(**MN** * **4**^**L**), где доска **MN** - размер доски, а **L** - длина слова **word**, **4** - разрешенные направления, так как всего клеток **MN** и для каждой мы будем вызывать **backtrack**, сложность которого **O**(**4**^**L**). Хотя оценка это оценка в наихудшем случае, в среднем алгоритм будет намного быстрее за счёт **backtracking**.

Сложность по памяти будет **O**(**L**) - это расходы на глубину рекурсии.

## Код:
```python
class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        def backtrack(i: int, j: int, word_idx: int) -> bool:
            if word_idx == len(word):
                return True

            if (
                i < 0
                or i >= len(board)
                or j < 0
                or j >= len(board[0])
                or board[i][j] != word[word_idx]
            ):
                return False

            temp = board[i][j]
            board[i][j] = ""

            if (
                backtrack(i + 1, j, word_idx + 1)
                or backtrack(i - 1, j, word_idx + 1)
                or backtrack(i, j + 1, word_idx + 1)
                or backtrack(i, j - 1, word_idx + 1)
            ):
                return True

            board[i][j] = temp
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i, j, 0):
                    return True

        return False


if __name__ == "__main__":
    f = Solution().exist
    print(
        f([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"),
    )
    print(f([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE"))
    print(f([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB"))

```

<div align='center'><h3><a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/106.Generate%20Parentheses'>⬅️ предыдущая задача</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/README.md'>Все задачи</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/108.Convert%20Sorted%20Array%20to%20Binary%20Search%20Tree'>следующая задача ➡️</a></h3></div>