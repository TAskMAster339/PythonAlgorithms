<div align='center'>
<h1><a href='https://leetcode.com/problems/find-k-pairs-with-smallest-sums/description/'><strong>123) Find K Pairs with Smallest Sums</strong></a></h1>
</div>

## **Условие:**

Даны два целочисленных массива **nums1** и **nums2** отсортированы в неубывающем порядке. И число **k**.

Верните **k** пар с наименьшей суммой, в которых одно число из первого массива, а оставшиеся из второго массива.

## **Идея:**

Воспользоваться **BFS**

## **Реализация:**

Создадим очередь с приоритетами, в которой будем хранить кортежи, которые состоят из суммы двух чисел, составляющих пары, индекс первого числа, индекс второго числа. В начале добавим туда кортеж (**nums1**[**0**] + **nums2**[**0**], **0**, **0**).

Далее пока в очереди есть хотя бы одна пара и пока мы еще не нашли **k** пар, мы будем извлекать из очереди наши три числа, нам понадобятся только индексы **i**, **j**. Добавляем с помощью индексов пары элементов в массив **result**. Затем добавляем в очередь (**i** + **1**, **j**) и (**i**, **j** + **1**), если они еще не встречались.

Таким образом мы постоянно будем поддерживать в очереди пары с минимальной суммой. Остаётся просто взять первые **k** из них и добавить в **result**.



## **Оценка:**

По времени наш алгоритм будет иметь сложность **O**(**K** * **logK**), где **K** - количество пар, которые нам нужно найти. (Цикл, в котором будет **K** итераций в каждой из которых будет либо добавляться, либо убираться элемент из кучи, что стоит **logK** операций)

По памяти мы займем **O**(**K**), расходы на очередь и множество.

## Код:
```python
import heapq


class Solution:
    def kSmallestPairs(
        self,
        nums1: list[int],
        nums2: list[int],
        k: int,
    ) -> list[list[int]]:
        if not nums1 and not nums2:
            return []

        pq = []
        heapq.heappush(pq, (nums1[0] + nums2[0], 0, 0))
        visited = set()
        result = []

        while pq and len(result) < k:
            _, i, j = heapq.heappop(pq)
            result.append((nums1[i], nums2[j]))
            if i + 1 < len(nums1) and (i + 1, j) not in visited:
                heapq.heappush(pq, (nums1[i + 1] + nums2[j], i + 1, j))
                visited.add((i + 1, j))
            if j + 1 < len(nums2) and (i, j + 1) not in visited:
                heapq.heappush(pq, (nums1[i] + nums2[j + 1], i, j + 1))
                visited.add((i, j + 1))

        return result


if __name__ == "__main__":
    f = Solution().kSmallestPairs
    print(f([1, 7, 11], [2, 4, 6], 3))
    print(f([1, 1, 2], [1, 2, 3], 2))

```

<div align='center'><h3><a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/122.IPO'>⬅️ предыдущая задача</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/README.md'>Все задачи</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/124.Find%20Median%20from%20Data%20Stream'>следующая задача ➡️</a></h3></div>