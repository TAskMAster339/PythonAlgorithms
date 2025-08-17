<div align='center'>
<h1><a href='https://leetcode.com/problems/find-median-from-data-stream/description/'><strong>124) Find Median from Data Stream</strong></a></h1>
</div>

## **Условие:**

Необходимо реализовать структуру данных **MedianFinder**, которая имеет конструктор, метод **void** **addNum**(**int** **num**), который добавляет число **num** в структуру данных, метод **double** **findMedian**(), который возвращает медиану всех чисел в структуре.

## **Идея:**

Та же самая идея, что и при реализации дека (**Double** **ended** **queue**)

## **Реализация:**

В конструкторе создадим две очереди с приоритетами, левую и правую. При добавлении элемента структуру мы будем добавлять элемент в левую очередь, при этом будем балансировать, чтобы обе очереди отличались максимум на **1** элемент. Заполняя такую структуру данных у нас будет две очереди с приоритетами, левая будет **MaxHeap**, в ней в корне кучи будет храниться число, находящиеся слева от центра, в правой кучи **MinHeap** будет храниться число, находящиеся справа от центра. Остаётся в методе **findMedian** возвращать или правое число, если суммарный размер куч нечетный, иначе сумма правого и левого числа, деленную пополам, потому что это и будет медиана последовательностью с чётной длинной.



## **Оценка:**

Сложность по времени метода **findMedian** будет **O**(**1**). Конструктор тоже будет **O**(**1**), а метод **addNum** будет иметь сложность **O**(**logN**), где **N** - количество элементов в структуре.

Сложность по памяти будет **O**(**N**).

## Код:
```python
import heapq


class MedianFinder:
    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.max_heap, -num)
        heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        if len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def findMedian(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        return (-self.max_heap[0] + self.min_heap[0]) / 2

```

<div align='center'><h3><a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/123.Find%20K%20Pairs%20with%20Smallest%20Sums'>⬅️ предыдущая задача</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/README.md'>Все задачи</a></h3></div>