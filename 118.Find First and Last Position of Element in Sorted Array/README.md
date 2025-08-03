<div align='center'>
<h1><a href='https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/'><strong>118) Find First and Last Position of Element in Sorted Array</strong></a></h1>
</div>

## **Условие:**

Дан массив целых чисел **nums**, отсортированный в неубывающем порядке. Найдите пару индексов первого появления и последнего появления числа **target**.

Если **target** не найден в массиве, следует вернуть [-**1**, -**1**].

Алгоритм должен быть быстрее линейного

## **Идея:**

Сначала найти **target** бинарным поиском, а потом с помощью бинарного поиска найти первое и последнее вхождение **target**

## **Реализация:**

Сначала с помощью бинарного поиска мы будем искать **target** в массиве. Как только мы нашли **target**, то попробуем продолжить искать другие **target**, которые расположены либо слева, либо справа от найденного центрального. Это делать будем тем же бинарным поиском.



## **Оценка:**

Верхняя граница по времени будет **O**(**logN**), так мы используем немного модифицированный бинарный поиск.

Верхняя оценка по памяти будет **O**(**1**).

## Код:
```python
class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def binary_search(is_left: bool):
            start, end, indx = 0, len(nums) - 1, -1

            while start <= end:
                mid = (start + end) // 2
                if nums[mid] < target:
                    start = mid + 1
                elif nums[mid] > target:
                    end = mid - 1
                else:
                    indx = mid
                    if is_left:
                        end = mid - 1
                    else:
                        start = mid + 1

            return indx

        left = binary_search(is_left=True)
        right = binary_search(is_left=False)
        return [left, right]


if __name__ == "__main__":
    f = Solution().searchRange
    print(f([5, 7, 7, 8, 8, 10], 8))  # [3, 4]
    print(f([5, 7, 7, 8, 8, 10], 6))  # [-1, -1]
    print(f([], 0))  # [-1, -1]

```

<div align='center'><h3><a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/117.Search%20in%20Rotated%20Sorted%20Array'>⬅️ предыдущая задача</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/README.md'>Все задачи</a></h3></div>