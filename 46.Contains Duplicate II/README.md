# [**46) Contains Duplicate II**](https://leetcode.com/problems/contains-duplicate-ii/description/)

## **Условие:**

Дан массив чисел **nums** и число **k**, нужно вернуть **True**, если в массиве есть два разных индекса **i** и **j**, такие что **nums**[**i**] == **nums**[**j**] и **abs**(**i** - **j**) <= **k**.

## **Идея:**

Пройдемся по массиву, заполняя хэш-таблицу, где ключ - число, а значение - его индекс.

## **Реализация:**

Идем по идее. Если мы встречаем число, которое уже есть в таблице, то мы проверяем, что растояние между его индексом и тем индексом, записанным в таблице, меньше или равно **k**, то возвращаем **True**.



## **Оценка:**

В наихудшем случае числа будут располагаться по краям массива, из-за этого верхняя граница по времени **O**(**N**), где **N** - длина массива. По памяти граница будет тоже **O**(**N**), так в наихудшем случае все числа, кроме двух, будут различны.

## Код:
```python
from typing import List
from util import test_case


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        table = dict()

        for i in range(len(nums)):
            if nums[i] in table:
                if i - table[nums[i]] <= k:
                    return True
            table[nums[i]] = i
        return False


if __name__ == "__main__":
    f = Solution().containsNearbyDuplicate
    test_case(f, True, nums=[1, 2, 3, 1], k=3)
    test_case(f, True, nums=[1, 0, 1, 1], k=1)
    test_case(f, False, [1, 2, 3, 1, 2, 3], k=2)

```

