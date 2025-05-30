<div align='center'>
<h1><a href='https://leetcode.com/problems/h-index/description/'><strong>11) H-Index</strong></a></h1>
</div>

Идея: посчитать все **h**-индексы и вернуть наибольший из них.

Сначала мы создадим массив **h_indexes**, длина которого будет на **1** больше, чем длина массива **citations**. Теперь мы пройдемся по массиву с цитатами, заполняя массив **h_indexes**, индексы в данном массиве - это все возможные **h** индексы, которые в теории можно получить из входного массива цитат. Так как может возникнуть ситуация, что например в массиве цитат: [**100**, **300**, **200**] **h** индекс равен **3**, так как длина массива **3**, которая является верхней границей **h** индекса, поэтому нам совершенно не важно количество цитат, если их количество превышает длину массива. Поэтому все работы с количеством цитат больше чем длина массива цитат, мы записываем их в последнюю ячейку массива **h_indexes**.

После этого цикла, мы создаем переменную **states**, в которой динамически будем считать количество статей. Затем мы проходим по массива **h_indexes** с помощью итератора **h** с конца так как нам нужно найти наибольший **h** индекс. Как только количество статей станет больше или равным **h** (итератор **h**, который находится в пределах от **0** до **len**(**citations**)), то это значит, что мы нашли искомый **h** индекс. При том такой индекс будет всегда найден, так как в последней итерации **h** == **0**, очевидно, количество статей, всегда будет более или равно **0**.

Сложность алгоритма **O**(**N**), также нужно будет хранить массив **h** индексов, поэтому потребуется память **O**(**N**).

## Код:
```python
from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        papers = len(citations)
        h_indexes = [0] * (papers + 1)

        for citation in citations:
            h_indexes[min(citation, papers)] += 1

        states = 0
        for h in range(papers, -1, -1):
            states += h_indexes[h]
            if states >= h:
                return h


# [] - 0
# [2] - 1 / [0] = 0
# [2, 17] = 2 - prev if current >= prev_h and current >= max_h else prev + 1
# [1, 29, 10] = 2
# [1, 29, 10, 2] = 2

# [0] = 0
# [0, 1, 2] =

# [1] = 1
# [1, 3] = 1
# [1, 3, 2] = 2

if __name__ == "__main__":
    s = Solution()
    print(s.hIndex([3, 0, 6, 1, 5]))
    print(s.hIndex([1, 3, 1]))
    print(s.hIndex([0, 1]))
    print(s.hIndex([11, 15]))

```

<div align='center'><h3><a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/10.Jump%20Game%20II'>⬅️ предыдущая задача</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/README.md'>Все задачи</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/12.Insert%20Delete%20GetRandom%20O(1)'>следующая задача ➡️</a></h3></div>