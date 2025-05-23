# [**2) Remove Element**](https://leetcode.com/problems/remove-element/description/)

Рофл: кринж а не задача, один раз пробегаем по массиву, копируя элементы не равные **val** в начало.

Создадим переменную **index**, которая будет указывать куда нам копировать элемент не равный **val**. Далее остается с помощью цикла **for** пройти по списку, проверяя следующие условие:

Если элемент списка не равен **val**, то мы копируем его в ячейку **index**, не забываем увеличить **index** на **1**. Также в задаче просят вернуть количество элементов, которые не равны **val**. Возвращаем **index**, так как он указывает индекс в который можно вписать новый элемент и так совпало, что его численное значение равно количеству ранее записанных в массив элементов.

Алгоритм проходит за **len**(**nums**), получаеться он линейный и его сложность **O**(**len**(**nums**)).

## Код:
```python
from typing import List


class Solution:
    def merge(
        self, nums1: List[int], m: int, nums2: List[int], n: int
    ) -> None:
        m, n, i = m - 1, n - 1, m + n - 1
        while n >= 0:
            if m >= 0 and nums1[m] > nums2[n]:
                nums1[i] = nums1[m]
                m -= 1
            else:
                nums1[i] = nums2[n]
                n -= 1
            i -= 1


if __name__ == "__main__":
    s = Solution()
    s.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
    s.merge([1], 1, [], 0)
    s.merge([0], 0, [1], 1)
    s.merge([1, 0], 1, [2], 1)

```

## Код:
```python
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1
        return index

```

