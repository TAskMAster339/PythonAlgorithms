<div align='center'>
<h1><a href='https://leetcode.com/problems/search-in-rotated-sorted-array/description/'><strong>117) Search in Rotated Sorted Array</strong></a></h1>
</div>

## **Условие:**

Дан массив целых чисел **nums**, отсортированный в возрастающем порядке. Все числа в нём различны.

При этом существует вероятность циклического сдвига массива **nums** на **k** вправо. Например, [**0**, **1**, **2**, **4**, **5**, **6**, **7**] может быть циклично сдвинут на **4** вправо [**4**, **5**, **6**, **7**, **0**, **1**, **2**].

Массив **nums** уже был циклически сдвинут, необходимо найти в нём число **target**. Необходимо вернуть индекс этого числа, или -**1**, если его нет в массиве.

Алгоритм должен быть быстрее **O**(**N**) по времени

## **Идея:**

Нужно как-то умно применить идею бинарного поиска

## **Реализация:**

Мы будем пользоваться следующей эвристикой: возьмем массив и разделим его пополам. Одна из половин всегда будет отсортированной (Попробуйте доказать это), если наш **target** находится в этой отсортированной половине, то мы можем с помощью классического бинарного поиска найти его там. Если наш **target** не находится в отсортированной половине, то мы повторяем этот алгоритм сначала, но уже на неотсортированной половине.

Действуя таким образом мы всегда будем двигать одни из двух указателей на середину массива, то есть мы будем сокращать нашу задачу всегда в два раза. Что позволит решить задачу быстрее, чем **O**(**N**).



## **Оценка:**

Так как мы делим задачу в два раза, то всего будет сделано **logN** действий, итого верхняя оценка по времени будет **O**(**logN**).

Верхняя оценка по памяти **O**(**1**).

## Код:
```python
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        start, end = 0, len(nums) - 1

        while start <= end:
            mid = (start + end) // 2

            if nums[mid] == target:
                return mid
            if nums[start] <= nums[mid]:
                if nums[start] <= target <= nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if nums[mid] <= target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1


if __name__ == "__main__":
    f = Solution().search
    print(f([4, 5, 6, 7, 0, 1, 2], 0))  # 4
    print(f([4, 5, 6, 7, 0, 1, 2], 3))  # -1
    print(f([1], 0))  # -1
    print(f([1, 3], 0))  # -1
    print(f([3, 1], 1))  # 1
    print(f([5, 1, 3], 1))  # 1

```

<div align='center'><h3><a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/116.Find%20Peak%20Element'>⬅️ предыдущая задача</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/README.md'>Все задачи</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/118.Find%20First%20and%20Last%20Position%20of%20Element%20in%20Sorted%20Array'>следующая задача ➡️</a></h3></div>