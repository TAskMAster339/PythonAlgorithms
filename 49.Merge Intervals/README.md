# [**49) Merge Intervals**](https://leetcode.com/problems/merge-intervals/description/)

## **Условие:**

Дан массив **intervals**, в котором **intervals**[**i**] = [**start**, **end**], нужно объединить пересекающиеся интервалы. Нужно вернуть массив непересекающихся интервалов, которые покрывают все интервалы входного массива.

## **Идея:**

Воспользоваться сортировкой.

## **Реализация:**

Отсортируем интервалы по их началу. Создадим массив **output**, который вернем. Добавим туда первый интервал.

Теперь в цикле мы будем проходить по оставшимся интервалам. Текущим интервалом будем называть последний в массиве **output** интервал. Если начало следующего интервала лежит в текущем, то мы изменяем значение конца текущего интервала на максимум из концов этих интервалов. Если начало следующего интервала больше предыдущего, то мы никак не можем объединить эти интервалы, поэтому добавляем новый интервал в **output**. И теперь этот интервал становиться текущим, с которым мы будем пытаться объединить последующие интервалы.



## **Оценка:**

По времени мы затратим **O**(**N** * **log** **N**) (из-за сортировки), по памяти **O**(**1**).

## Код:
```python
from typing import List
from util import test_case


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:  # so bad
        intervals.sort(key=lambda arr: arr[0])
        left = 0
        right = 1
        while right < len(intervals):
            first = intervals[left]
            second = intervals[right]
            if second[0] <= first[1]:
                newLine = [first[0], max(second[1], first[1])]
                intervals.pop(right)
                intervals[left] = newLine
            else:
                left += 1
                right += 1
        return intervals

    def merge2(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i: i[0])
        output = [intervals[0]]

        for start, end in intervals[1:]:
            lastEnd = output[-1][1]
            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])
        return output


if __name__ == "__main__":
    f = Solution().merge
    test_case(
        f, [[1, 6], [8, 10], [15, 18]], [[1, 3], [2, 6], [8, 10], [15, 18]]
    )
    test_case(f, [[1, 5]], [[1, 4], [4, 5]])
    test_case(f, [[1, 3]], [[1, 3]])
    test_case(f, [[1, 4], [5, 6]], [[1, 4], [5, 6]])
    test_case(f, [[0, 5]], [[1, 4], [0, 2], [3, 5]])

```

### [<-- предыдущая задача](https://github.com/TAskMAster339/PythonAlgorithms/tree/main/48.Summary%20Ranges) | [следующая задача -->](https://github.com/TAskMAster339/PythonAlgorithms/tree/main/50.Insert%20Interval)
