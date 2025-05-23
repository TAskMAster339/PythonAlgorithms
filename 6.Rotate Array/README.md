# [**6) Rotate Array**](https://leetcode.com/problems/rotate-array/description/)

Идея: использовать инверсию.

Наша задача сделать циклический сдивг массива. Для этого сначала разделим размер сдвига **k** на длину списка **len**(**nums**) по модулю. Сильная экономия так как результат сдвига массива с **10** элементами или на **1**, или на **11**, или на **21** и т. д будет одинаковым.

Самое эффективное и простое решение - сделать три инверсии массива. Во-первых, мы инвертируем весь массив. Во-вторых, инвертируем элементы с начала массива до **k**. В-третьих, инвертируем элементы с **k** до конца. Вуаля, решение готово. Осталось только реализовать функцию инверсии. Функция **invert** будет принимать массив, индекс старта диапазона инверсии, индекс конца диапазона. В самой фукции мы будем менять пары элементов: первый с последним, второй с предпоследним и т. д.

Первая инверсия пройдет половину массива и потребует **O**(**n**/**2**) времени, вторая **O**(**k**/**2**), третья **O**((**n**-**k**)/**2**). После отбрасывания коэффицентов и констант, поучим **O**(**n**) + **O**(**1**) + **O**(**n**) = **2O**(**n**) = **O**(**n**).

Время алгоритма - линейное **O**(**n**).

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

## Код:
```python
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 1
        w = 0
        flag = True
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                count += 1
            else:
                count = 1
            if count > 2 and flag:
                w = i + 1
                flag = False
            if w != 0 and count <= 2:
                nums[w] = nums[i + 1]
                w += 1
        if w == 0:
            return len(nums)
        return w

    def removeDuplicates2(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)

        slow = 2

        for fast in range(2, len(nums)):
            if nums[fast] != nums[slow - 2]:
                nums[slow] = nums[fast]
                slow += 1

        return slow


if __name__ == "__main__":
    s = Solution()
    print(s.removeDuplicates([1, 1, 1, 2, 2, 3]))
    print(s.removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3]))

```

## Код:
```python
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        result = 0
        count = 0

        for i in nums:
            if count == 0:
                result = i

            count += 1 if i == result else -1

        return result


if __name__ == "__main__":
    s = Solution()
    print(s.majorityElement([3, 2, 3]))
    print(s.majorityElement([2, 2, 1, 1, 1, 2, 2]))

```

## Код:
```python
from typing import List


def invert(nums, start, end):
    for i in range(start, (start + end) // 2):
        nums[i], nums[end - 1] = nums[end - 1], nums[i]
        end -= 1


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k %= len(nums)
        invert(nums, 0, len(nums))
        invert(nums, 0, k)
        invert(nums, k, len(nums))


if __name__ == "__main__":
    s = Solution()
    s.rotate([1, 2, 3, 4, 5, 6, 7], 3)
    s.rotate([-1, -100, 3, 99], 2)

```

