<div align='center'>
<h1><a href='https://leetcode.com/problems/surrounded-regions/description/'><strong>90) Surrounded Regions</strong></a></h1>
</div>

## **Условие:**

Дана матрица **board** **m** на **n**, которая состоит из букв '**X**' и '**O**', нужно захватить области, которые окружены.

Соединения - ячейки, которые соединены по вертикали или горизонтали с соседями.

Область - соединение ячеек, содержащих '**O**'.

Окружение - область, окруженная '**X**', если все ячейки '**X**' из окружения можно соединить и ни одна из ячеек '**O**' области не находится на краю доски.

Чтобы захватить окруженную область, нужно заменить все '**O**' в ней на '**X**'. Сделать это нужно на месте

## **Идея:**

Пойти от обратного

## **Реализация:**

Заметим, что если любое множество нулей расположено где-то внутри матрицы, то есть оно никак не касается её краев, то мы всегда окружим эту область и заменим все нули на крестики. Остается только найти нули, которые расположены по краям матрицы и пометить области, к которым они принадлежат, чтобы оставить их нулями.

Создадим очередь. В очередь запишем координаты всех нулей, которые расположены по краям матрицы. Далее с помощь **BFS** мы пройдемся по всем нулям, соединяя их в область. При этом каждый нуль в области будем заменять каким-либо специальным символом.

После такого прохода на доске останутся нули, крестики и специальные символы. Осталось заменить все нолики на крестики, а спец символы на нолики, тогда мы получим ответ.



## **Оценка:**

Верхняя граница по времени будет **O**(**NM**), где **N**, **M** - размеры матрицы. (Обход матрицы по краю даст **max**(**O**(**N**), **O**(**M**)), **BFS** в наихудшем случае займет **O**(**NM**), выбираем наибольшую оценку). По памяти мы затратим **O**(**NM**), в наихудшем случае очередь будет полностью заполнена.

## Код:
```python
class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        queue = []

        for i in range(m):
            if board[i][0] == "O":
                queue.append((i, 0))
            if board[i][n - 1] == "O":
                queue.append((i, n - 1))

        for j in range(n):
            if board[0][j] == "O":
                queue.append((0, j))
            if board[m - 1][j] == "O":
                queue.append((m - 1, j))

        while queue:
            cur_r, cur_c = queue.pop(0)
            board[cur_r][cur_c] = "*"
            for dr, dc in directions:
                new_r = cur_r + dr
                new_c = cur_c + dc
                if 0 <= new_r < m and 0 <= new_c < n and board[new_r][new_c] == "O":
                    queue.append((new_r, new_c))

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "*":
                    board[i][j] = "O"



if __name__ == "__main__":
    s = Solution()
    target = [
            ["X","X","X","X"],
            ["X","O","O","X"],
            ["X","X","O","X"],
            ["X","O","X","X"],
        ]
    s.solve(target)

    for row in target:
        print(row)


```

<div align='center'><h3><a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/89.Number%20of%20Islands'>⬅️ предыдущая задача</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/README.md'>Все задачи</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/91.Clone%20Graph'>следующая задача ➡️</a></h3></div>