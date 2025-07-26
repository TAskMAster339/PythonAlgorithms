<div align='center'>
<h1><a href='https://leetcode.com/problems/construct-quad-tree/description/'><strong>110) Construct Quad Tree</strong></a></h1>
</div>

## **Условие:**

Дана матрица **grid** размером **n** **x** **n**, состоящая из **0** и **1**. Мы хотим превратить матрицу в **Quad**-**Tree**. Нужно вернуть построенное **Quad**-**Tree**.

**Quad**-**Tree** - структура данных, в которой каждый узел имеет ровно **4** наследника и **2** атрибута: **val** значение и **isLeaf** булева переменная, показывая является ли узел листом. Подробнее в **https**://**en**.**wikipedia**.**org**/**wiki**/**Quadtree**. Еще смотрите картинку

## **Идея:**

Задачу очень легко можно разделить на подобную более простую задачу

## **Реализация:**

Классическая задача для презентации подхода "Разделяй и Властвуй".

В процессе разделения мы будем делить задачу на **4** части, потому что **Quad**-**Tree** состоит из **4** поддеревьев, которые тоже являются **Quad**-**Tree**.

Когда мы дойдем до **Quad**-**Tree** размером **1**, то мы будем заниматься властвованием, объединением малых поддеревьев в большие.

Реализуется это через простую рекурсию:

Крайний случай - когда размер нашей сетки **grid** равен **1** **x** **1**. Тогда мы возвращаем узел без детей с единственным значением, которое есть в **grid**, **isLeaf** ставим **True**, так как это самое маленькое поддерево, оно очевидно должно быть листом.

Рекуррентный случай - **4** раза вызываем нашу функцию на уже на срезах массива, каждый из которых представляет собой либо, верхний левый квадрат матрицы, либо верхний правый квадрат матрицы, либо нижний левый квадрат матрицы, либо нижний правый квадрат матрицы.

Если все из них имеют одинаковое значение и при этом все листы, то мы можем их объединить в один узел, который будет иметь значения одного из поддеревьев (не важно какого, они все будут равны), и тоже будет листом.

Иначе мы возвращаем новый узел, который будет иметь значение **1**, **isLeaf** = **False**, и **4** ранее созданных наследника (поддерева).



## **Оценка:**

Верхняя оценка по памяти будет **O**(**N**^**2**), так как мы в наихудшем случае создадим узел для каждого числа в матрицы размером **N** **x** **N**. Хотя эту память можно признать полезной, тогда дополнительной памяти будет затрачено **O**(**logN**) на глубину рекурсии.

Верхняя оценка по времени будет **O**(**N**^**2**), потому что в наихудшем случае алгоритм пройдет во всем числам матрицы, что будет стоить **O**(**N**^**2**). При этом мы не учитываем расходы на создание подматриц (копирование массивов). С ними получиться **O**(**N**^**2** * **log** **N**). Но это легко поправимо, если передавать ссылки на **view** матрицы, а не множить копии.

## Код:
```python
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: list[list[int]]) -> Node:
        if len(grid) == 1:
            return Node(grid[0][0], True, None, None, None, None)
        n = len(grid) // 2
        topLeft = self.construct([row[:n] for row in grid[:n]])
        topRight = self.construct([row[n:] for row in grid[:n]])
        bottomLeft = self.construct([row[:n] for row in grid[n:]])
        bottomRight = self.construct([row[n:] for row in grid[n:]])
        if (topLeft.val == topRight.val == bottomLeft.val == bottomRight.val) and (
            topLeft.isLeaf
            and topRight.isLeaf
            and bottomLeft.isLeaf
            and bottomRight.isLeaf
        ):
            return Node(topLeft.val, isLeaf=True)
        return Node(1, False, topLeft, topRight, bottomLeft, bottomRight)


if __name__ == "__main__":
    X = [
        [1, 1, 0, 0],
        [0, 0, 1, 1],
        [1, 1, 0, 0],
        [0, 0, 1, 1],
    ]
    Y = [[1, 1], [0, 0]]
    n = len(Y) // 2
    print([row[:n] for row in Y[:n]])
    print([row[n:] for row in Y[:n]])
    print([row[:n] for row in Y[n:]])
    print([row[n:] for row in Y[n:]])

```

<div align='center'><h3><a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/109.Sort%20List'>⬅️ предыдущая задача</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/README.md'>Все задачи</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/111.Merge%20k%20Sorted%20Lists'>следующая задача ➡️</a></h3></div>