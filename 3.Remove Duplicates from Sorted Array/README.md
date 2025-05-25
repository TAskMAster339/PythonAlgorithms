<div align='center'>
<h1><a href='https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/'><strong>3) Remove Duplicates from Sorted Array</strong></a></h1>
</div>

Идея: Делаем один проход по массиву, сравнивая пары.

Так как по условию список отсортирован по не убыванию, то все дубликаты будут расположенны рядом друг с другом! Создадим итератор **j**, который будем использовать для записи элементов. Он равен **1**, так как **0** элемент сам по себе будет уникальным (Его дубликаты могут появиться только с **1** элемента). Так мы немного сэкономим.

Затем итерируемся по списку, начиная с **1** элемента, заканчивая последним. (Это нужно для сравнения пар (**i**, **i**-**1**))

Если элементы в паре не равны, то мы копируем **i**-тый элемент в **j**-тую ячейку. Инкрементируем **j**. Затем в задаче требуется вернуть количество уникальных элементов, аналогично предыдущей задачи их количество будет равно **j**.

Вообще задача прикольная, рекомендую с помощью дебаггера пошагово посмотреть как он сдвигает уникальные элементы в начало.

Так как мы делаем один цикл **for** с **len**(**nums**) - **1** итерацией, то сложность алгоритма **O**(**len**(**nums**)-**1**)

## Код:
```python
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
        return j

```

<div align='center'><h3><a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/2.Remove%20Element'>⬅️ предыдущая задача</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/README.md'>Все задачи</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/4.Remove%20Duplicates%20from%20Sorted%20Array%20II'>следующая задача ➡️</a></h3></div>