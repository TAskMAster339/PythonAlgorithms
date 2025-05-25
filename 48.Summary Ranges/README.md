# [**48) Summary Ranges**](https://leetcode.com/problems/summary-ranges/description/)

## **Условие:**

Дан отсортированный массив **nums**, состоящий из уникальных элементов.

Нужно вернуть наименьший отсортированный список отрезков, которые вместе покрывают все числа массива. Например,

[**0**, **1**, **2**, **3**, **4**, **5**, **7**] -> ["**0**->**2**", "**4**->**5**", "**7**"]

Здесь под отрезком [**a**, **b**] понимается - множество целых чисел в диапазоне [**a**, **b**], включая **a** и **b**

## **Идея:**

Нужно просто проинтерпретировать массив в массив отрезков. Очень удобно сделать это жадно.

## **Реализация:**

Создадим два указателя. Один будет указывать на начало отрезка, второй на конец. Второй будет двигаться до тех пор, пока мы можем сделать отрезок. Как только мы встретили число, которое не может войти в данный промежуток, то мы добавляем его в список. Не забываем обработать отрезки, в которых начало равно концу. Так как массив отсортирован и мы каждый раз делаем жадный выбор, то в итоге мы получим наименьший отсортированый массив отрезков.



## **Оценка:**

По времени мы получим **O**(**N**), по памяти **O**(**1**).

## Код:
```python
from typing import List
from util import test_case


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        result = []
        left = 0
        right = 1
        while left != right:
            if right < len(nums) and nums[right] - nums[right - 1] > 1:
                if nums[left] == nums[right - 1]:
                    string = f"{nums[left]}"
                else:
                    string = f"{nums[left]}->{nums[right - 1]}"
                result.append(string)
                left = right
            if right <= len(nums) - 1:
                right += 1
            else:
                if nums[left] == nums[right - 1]:
                    string = f"{nums[left]}"
                else:
                    string = f"{nums[left]}->{nums[right - 1]}"
                result.append(string)
                left = right
        return result


if __name__ == "__main__":
    f = Solution().summaryRanges
    test_case(f, ["0->2", "4->5", "7"], [0, 1, 2, 4, 5, 7])
    test_case(f, ["0", "2->4", "6", "8->9"], [0, 2, 3, 4, 6, 8, 9])

```

### [<-- предыдущая задача](https://github.com/TAskMAster339/PythonAlgorithms/tree/main/47.Longest%20Consecutive%20Sequence) | [следующая задача -->](https://github.com/TAskMAster339/PythonAlgorithms/tree/main/49.Merge%20Intervals)
