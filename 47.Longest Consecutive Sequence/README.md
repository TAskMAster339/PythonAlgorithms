# [**47) Longest Consecutive Sequence**](https://leetcode.com/problems/longest-consecutive-sequence/description/)

## **Условие:**

Дан неотсортированный массив **nums**, нужно вернуть длину наибольшей последовательности подряд идущих чисел. Например, [**100**, **4**, **200**, **1**, **3**, **2**] -> **1**, **2**, **3**, **4**, поэтому ответ **4**.

## **Идея:**

Нужно впихнуть два указателя в хэш-таблицу.

## **Реализация:**

Создадим хэш-таблицу. Затем пройдемся по всем элементам множества из **nums**, так как нам нет смысла рассматривать дубликаты. В таблице будем хранить число из **nums** в качестве ключа, а значением будет длина наибольшей последовательности в которую они входят. Длина будет равна сумме длин левой **num** - **1** и правой **num** + **1** последовательности. Остается не забыть обновить значение на краях последовательности. Таким образом бы будем относительно каждого числа расширить последовательность вправо и влево. Будем при этом динамически считать максимальную длину. Её мы вернем в конце.



## **Оценка:**

По времени мы потратим **O**(**N**), по памяти **O**(**N**).

## Код:
```python
from typing import List
from util import test_case


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        table = {}
        result = 0
        for num in nums:
            left = table.get(num - 1, 0)
            right = table.get(num + 1, 0)
            length = left + right + 1
            table[num - left] = length
            table[num + right] = length
            result = max(result, length)
        return result


if __name__ == "__main__":
    f = Solution().longestConsecutive
    test_case(f, 4, nums=[100, 4, 200, 1, 3, 2])
    test_case(f, 9, nums=[0, 3, 7, 2, 5, 8, 4, 6, 0, 1])

```

### [<-- предыдущая задача](https://github.com/TAskMAster339/PythonAlgorithms/tree/main/46.Contains%20Duplicate%20II) | [следующая задача -->](https://github.com/TAskMAster339/PythonAlgorithms/tree/main/48.Summary%20Ranges)
