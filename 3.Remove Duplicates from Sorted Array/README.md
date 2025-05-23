# [**3) Remove Duplicates from Sorted Array**](https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/)

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

