# [**51) Minimum Number of Arrows to Burst Balloons**](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/description/)

## **Условие:**

Есть несколько сферических шаров, представленных в плоскости **XY**. Шары представлены как массив чисел **points**, где **points**[**i**] = [**x_start**, **x_end**] - горизонтальный диаметр шара. **Y** координаты точно не известны. (Нам они и не нужны)

Вам даны стрелы, которыми можно стрелять строго вверх из любой точки, лежащей на оси **X**. Шар с координатам [**x_start**, **x_end**] лопается из-за стрелы, выпущенной в точке **x**, если **x_start** <= **x** <= **x_end**. Количество стрел бесконечно. Летят они вверх тоже бесконечно.

Нужно вернуть минимальное количество стрел, которого достаточно, чтобы лопнуть все шары.

## **Идея:**

Задача сводится к поиску количества ненулевых пересечений данных отрезков.

## **Реализация:**

Наша задача - пытаться лопнуть одной стрелой как можно больше шаров. Поэтому отсортируем их по **x_start**. И будем пытаться пересечь первый промежуток с как можно большим количеством других. Как только мы нашли такой отрезок, который не можем лопнуть вместе с предыдущими, то мы понимаем, что нам нужна еще как минимум одна стрела, продолжаем тот же алгоритм только уже с этим промежутком.



## **Оценка:**

Из-за сортировки по времени мы затратим **O**(**N** * **log** **N**), по памяти **O**(**1**).

## Код:
```python
from typing import List
from util import test_case


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points.sort(key=lambda x: x[1])

        union = []
        start = points[0][0]
        end = points[0][1]
        for x, y in points[1:]:
            if end < x:
                union.append([start, end])
                start = 0
                end = float("inf")
            start = max(start, x)
            end = min(end, y)
        union.append([start, end])

        return len(union)

    def findMinArrowShots2(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points.sort(key=lambda x: x[1])
        prev = points[0]
        total = 1
        for i in points[1:]:
            if prev[1] < i[0]:
                prev = i
                total += 1
        return total


if __name__ == "__main__":
    f = Solution().findMinArrowShots2
    test_case(f, 2, points=[[10, 16], [2, 8], [1, 6], [7, 12]])
    test_case(f, 4, [[1, 2], [3, 4], [5, 6], [7, 8]])
    test_case(f, 2, points=[[1, 2], [2, 3], [3, 4], [4, 5]])
    test_case(f, 0, [])
    test_case(f, 2, [[1, 2], [4, 5], [1, 5]])
    test_case(
        f,
        2,
        [
            [3, 9],
            [7, 12],
            [3, 8],
            [6, 8],
            [9, 10],
            [2, 9],
            [0, 9],
            [3, 9],
            [0, 6],
            [2, 8],
        ],
    )

```

