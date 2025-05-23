# [**30) Minimum Size Subarray Sum**](https://leetcode.com/problems/minimum-size-subarray-sum/description/)

## **Условие:**

Дан массив натуральных чисел **nums** и число **target**, нужно вернуть минимальную длину подмассива, сумма котором больше или равна **target**. Если такого подмассива нет, нужно вернуть **0**.

Подмассив - это непрерывная непустая последовательность элементов внутри массива. Например, [**1**,**2**,**3**,**4**,**5**] -> [**3**,**4**,**5**]

## **Идея:**

Будем с помощью двух указателей искать наименьший подмассив

## **Реализация:**

Создадим указатели **left** = **0** и **right** = **0**, также переменную **cur_sum** = **nums**[**left**], в которой динамически будем считать сумму. В **min_len** мы будем хранить наименьшую длину подмассива.

В цикле будем проверять: если **cur_sum** >= **target**, то обновляем **min_len** и двигаем левый указатель, не забывая изменить при этом сумму. Иначе мы двигаем правый указатель, добавляя его значение в сумму.



## **Оценка:**

Один цикл говорит о верхней границы по времени в **O**(**N**), также было задействовано константное количество памяти **O**(**1**).

## Код:
```python
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        cur_sum = nums[left]
        min_len = float("inf")

        while right != len(nums) - 1 or left != len(nums):
            if cur_sum >= target:
                min_len = min(min_len, right - left + 1)
                cur_sum -= nums[left]
                left += 1
                continue
            else:
                right += 1
                if right >= len(nums):
                    return min_len if min_len != float("inf") else 0
            cur_sum += nums[right]
        return min_len if min_len != float("inf") else 0


if __name__ == "__main__":
    s = Solution()
    print(s.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
    print(s.minSubArrayLen(4, [1, 4, 4]))
    print(s.minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]))
    print(s.minSubArrayLen(11, [1, 2, 3, 4, 5]))  # 3
    print(s.minSubArrayLen(7, [1, 1, 1, 1, 7]))

```

