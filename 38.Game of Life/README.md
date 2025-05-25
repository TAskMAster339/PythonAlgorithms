# [**38) Game of Life**](https://leetcode.com/problems/game-of-life/description/)

## **Условие:**

Нужно реализовать игру "Жизнь", созданную Джоном Хортоном Конвейем.

Правила следующие: есть игровая доска, представленная матрицей **m** на **n**, в каждой клетке которой находится либо **0** (смерть), либо **1** (жизнь) Каждая клетка взаимодействует с восемью своими соседями по следующим принципам:

**1**) Любая живая клетка с менее двумя живыми соседями умирает, из-за маленькой популяции.

**2**) Любая живая клетка с двумя или тремя живыми соседями доживает до следующего поколения.

**3**) Любая живая клетка с четырьмя и более живыми соседями умирает, из-за перенаселения

**4**) Любая мертвая клетка, может стать живой, если среди её соседей есть ровно три живых клетки.

## **Идея:**

Очень похожа на предыдущую задачу. Нужно просто отметить клетки, которые в следующей итерации погибнут или станут живыми.

## **Реализация:**

Пройдемся по всем клеткам, считая их живых соседей. После окончания подсчета применяем правила игры к этой клетке. (Либо ничего не делаем, либо заменяем её на символ, который означает, что это будущая **1**, или будущий **0**).

В конце с помощью еще одного цикла заменяем все знаки нуля на **0**, а все знаки единицы на **1**.



## **Оценка:**

Сложность по времени будет **O**(**N** * **M**) (Циклы, которые отвечают за подсчет соседей можно считать константными). По памяти мы затратим **O**(**1**).

## Код:
```python
from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        zero_sign = "*"
        one_sign = "$"

        for i in range(len(board)):
            for j in range(len(board[i])):
                count_one = 0
                for di in range(-1, 2):
                    for dj in range(-1, 2):
                        if -1 < i + di < len(board) and -1 < j + dj < len(
                            board[i]
                        ):
                            if di == 0 and dj == 0:
                                continue
                            if (
                                board[i + di][j + dj] == 1
                                or board[i + di][j + dj] == zero_sign
                            ):
                                count_one += 1

                if board[i][j] == 1:
                    if count_one < 2 or count_one > 3:
                        board[i][j] = zero_sign
                        continue
                if board[i][j] == 0:
                    if count_one == 3:
                        board[i][j] = one_sign
                        continue

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == zero_sign:
                    board[i][j] = 0
                if board[i][j] == one_sign:
                    board[i][j] = 1


if __name__ == "__main__":
    s = Solution()
    board1 = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
    s.gameOfLife(board1)
    Output1 = [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]
    print(board1)
    board2 = [[1, 1], [1, 0]]
    s.gameOfLife(board2)
    Output2 = [[1, 1], [1, 1]]
    print(board2)

```

### [<-- предыдущая задача](https://github.com/TAskMAster339/PythonAlgorithms/tree/main/37.Set%20Matrix%20Zeroes) | [следующая задача -->](https://github.com/TAskMAster339/PythonAlgorithms/tree/main/39.Ransom%20Note)
