# [**2) Remove Element**](https://leetcode.com/problems/remove-element/description/)

Рофл: кринж а не задача, один раз пробегаем по массиву, копируя элементы не равные **val** в начало.

Создадим переменную **index**, которая будет указывать куда нам копировать элемент не равный **val**. Далее остается с помощью цикла **for** пройти по списку, проверяя следующие условие:

Если элемент списка не равен **val**, то мы копируем его в ячейку **index**, не забываем увеличить **index** на **1**. Также в задаче просят вернуть количество элементов, которые не равны **val**. Возвращаем **index**, так как он указывает индекс в который можно вписать новый элемент и так совпало, что его численное значение равно количеству ранее записанных в массив элементов.

Алгоритм проходит за **len**(**nums**), получаеться он линейный и его сложность **O**(**len**(**nums**)).

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

### [<-- предыдущая задача](https://github.com/TAskMAster339/PythonAlgorithms/tree/main/1.Merge%20Sorted%20Array) | [следующая задача -->](https://github.com/TAskMAster339/PythonAlgorithms/tree/main/3.Remove%20Duplicates%20from%20Sorted%20Array)
