<div align='center'>
<h1><a href='https://leetcode.com/problems/max-points-on-a-line/description/'><strong>136) Max Points on a Line</strong></a></h1>
</div>

## **Условие:**

Дан массив точек **points**, где **points**[**i**] = [**x_i**, **y_i**] представляет собой точку в **XY** плоскости. Необходимо вернуть максимальное количество точек, которые лежат на одной прямой

## **Идея:**

Вспомнить, как в геометрии понимают, что точки лежат на одной прямой

## **Реализация:**

Прямая задается уравнением **y** = **kx** + **b**, если у двух прямых, два одинаковых коэффициента **k**, то они либо параллельны, либо являются одной и той же прямой.

Будем перебирать все возможные пары точек, и составлять словарь, в котором ключом будет значение коэффициента **k**, а значением, количество точек с таким коэффициентом. Таким перебором мы избежим случаи, когда точки могут лежать на параллельных прямых. Остается загуглить формулу **k** и решение готово.



## **Оценка:**

По времени алгоритм будет **O**(**N**^**2**), так как мы переберем все возможные пары точек. По памяти мы затратим **O**(**N**), так как в худшем случае у нас будут только **2** точки на одной прямой, поэтому в словаре будет **N** различных коэффициентов **k**.

## Код:
```python
from collections import defaultdict


class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        if len(points) <= 2:
            return len(points)

        def slope(p1, p2):
            if p1[0] == p2[0]:
                return float("inf")
            return (p2[1] - p1[1]) / (p2[0] - p1[0])

        ans = 1

        for i, p1 in enumerate(points):
            slopes = defaultdict(int)
            for _, p2 in enumerate(points[i + 1 :]):
                slp = slope(p1, p2)
                slopes[slp] += 1
                ans = max(ans, slopes[slp])
        return ans + 1


if __name__ == "__main__":
    f = Solution().maxPoints
    print(f([[1, 1], [2, 2], [3, 3]]))  # 3
    print(f([[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]))  # 4

```

<div align='center'><h3><a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/135.Pow(x,%20n)'>⬅️ предыдущая задача</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/README.md'>Все задачи</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/137.Climbing%20Stairs'>следующая задача ➡️</a></h3></div>