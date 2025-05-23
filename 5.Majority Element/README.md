# [**5) Majority Element**](https://leetcode.com/problems/majority-element/description/)

Идея: ищем моду, в условии дана огромная подсказка как это сделать за один пробег.

Решение следующие. Во-первых, мы, прочитав условие, понимаем, что самый частый элемент в массиве (мода) встречается более **n** / **2** раз, где **n** - длина массива. Во-вторых, мы делаем вывод, что если мы создадим счетчик, который будет инкрементироваться каждый раз, когда мы встречаем моду и декрементироваться каждый раз при встрече другого числа. То такой счетчик всегда будет больше **0**. (Подумайте об этом, это очень важно)

Итак, мы создадим переменную **result**, в которую запишем искомую моду, и счетчик **count**. После этого пройдем по массиву циклом **for**-**each**. Кажую итерацию мы будем сравнивать **i** == **result**, если они равны, то мы делаем **count** += **1**, иначе **count** -= **1**. Далее важный момент - **count** == **0**, это значит, что мы нашли вторую "моду" (на данный момент цикла она будет такой же модой, как и перая), значит в **result** нужно присвоить новонайденную моду(не факт, что она правильная). Таким образом у нас будет постоянная происходить гонка мод, но благодаря условию, что самый частый элемент встречается более чем **n** / **2** раз, мы можем быть спокойны и уверены, что в коцне концов настоящая мода победит и будет записанна в **result**.

Сложность алгоритма - **O**(**n**), где **n** - длина массива.

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

