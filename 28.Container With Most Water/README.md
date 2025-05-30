<div align='center'>
<h1><a href='https://leetcode.com/problems/container-with-most-water/description/'><strong>28) Container With Most Water</strong></a></h1>
</div>

## **Условие:**

Дан массив чисел **height** длины **n**, в котором **n** вертикальных линий, представляющие собой отрезок. **i**-тая линия это отрезок с двумя точками (**i**, **0**) и (**i**, **height**[**i**]). Нужно найти две линии, которые вместе с осью **x** формируют контейнер, содержащий наибольшее количество воды. Нужно вернуть это количество воды.

## **Идея:**

Намудрили дофига. Проще говоря, нужно найти наибольший прямоугольник, состоящий из оси **x** и двух линий. Вернуть нужно его площадь.

## **Реализация:**

Создадим два указателя **left** = **0** и **right** = **len**(**height**) - **1**. Также создадим переменную **maxArea**, в которой будем считать максимальную площадь, её мы вернем в конце программы.

Почему указатели опять так расположены? Потому что наша задача найти наибольшую площадь прямоугольника (**S** = **a** * **b**), для этого максимизируем сторону, которая определяется осью **x**. Её длина будет равна разности **right** - **left**. Она будет максимальная когда **right** = **len**(**height**) - **1**, **a** **left** = **0**. Теперь мы будем двигать указатели, при этом каждый раз заново пересчитывая площадь. Двигать мы будем по следующей логики: мы будем пытаться максимизировать длину линии. (Двигая указатель мы уменьшаем длину одной стороны, поэтому мы хотим, чтобы другая сторона при этом выросла).

Таким образом мы рассмотрим все возможные пары линий, где **left** < **right**.

После данного процесса у нас останется максимальная площадь, записанная в **maxArea**.



## **Оценка:**

По памяти мы потратим **O**(**1**), по времени **O**(**N**).

## Код:
```python
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        left, right = 0, len(height) - 1
        while left < right:
            maxArea = max(
                maxArea, min(height[left], height[right]) * (right - left)
            )
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxArea


if __name__ == "__main__":
    s = Solution()
    print(s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
    print(s.maxArea([1, 1]))

```

<div align='center'><h3><a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/27.Two%20Sum%20II%20-%20Input%20Array%20Is%20Sorted'>⬅️ предыдущая задача</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/README.md'>Все задачи</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/29.3Sum'>следующая задача ➡️</a></h3></div>