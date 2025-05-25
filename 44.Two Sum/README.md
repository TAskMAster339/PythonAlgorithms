# [**44) Two Sum**](https://leetcode.com/problems/two-sum/description/)

## **Условие:**

Дан массив чисел **nums** и число **target**, нужно вернуть массив из двух индексов чисел, которые необходимо сложить, чтобы получить **target**. Решение единственное.

## **Идея:**

Нужно воспользоваться единственностью решения.

## **Реализация:**

Так как нам гарантируют, что решение одно, то мы можем сделать вывод, что те, числа, которые в сумме дают **target**, находятся в массиве ровно в одном экземпляре. Воспользовавшись этой идей, мы создадим хэш-таблицу, в которой ключом будет число, а значением его индекс.

Затем пройдемся по всем элементам снова, теперь мы будем рассматривать не само число, а его предполагаемую пару: **pair_element** = **target** - **nums**[**i**], если это число есть в таблице и его индекс не равен индексу **i**, то мы нашли нашу пару индексов, возвращаем [**i**, **table**[**pair_element**]]



## **Оценка:**

По времени мы потратим **O**(**N**), по памяти мы потратим **O**(**N**).

## Код:
```python
from typing import List
from util import test_case


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = dict()
        for i in range(len(nums)):
            table[nums[i]] = i

        for i in range(len(nums)):
            pair_element = target - nums[i]
            if pair_element in table and table[pair_element] != i:
                return [i, table[pair_element]]


if __name__ == "__main__":
    f = Solution().twoSum
    test_case(f, [0, 1], nums=[2, 7, 11, 15], target=9)
    test_case(f, [1, 2], nums=[3, 2, 4], target=6)
    test_case(f, [0, 1], nums=[3, 3], target=6)

```

### [<-- предыдущая задача](https://github.com/TAskMAster339/PythonAlgorithms/tree/main/43.Group%20Anagrams) | [следующая задача -->](https://github.com/TAskMAster339/PythonAlgorithms/tree/main/45.Happy%20Number)
