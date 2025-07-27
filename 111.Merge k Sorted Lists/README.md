<div align='center'>
<h1><a href='https://leetcode.com/problems/merge-k-sorted-lists/description/'><strong>111) Merge k Sorted Lists</strong></a></h1>
</div>

## **Условие:**

Дан массив, состоящий из **k** связных списков, **lists**, каждый связный список отсортирован в возрастающем порядке. Необходимо объединить все **k** связных списков в один и вернуть его

## **Идея:**

Если вы знаете как объединить **2** связных списка, то эту идею очень легко обобщить до объединения **k** связных списков

## **Реализация:**

Сначала реализуем процедуру, которая объединяет два списка вместе. Это всего лишь движение двух указателей по спискам и поочередное добавление наименьшего числа в паре в объединённый список.

Теперь для того, чтобы объединить **k** связных списков, нам необходимо как-то упростить нашу задачу (разделить её на подзадачи) и затем властнуть тогда, когда количество списков будет равно **2**.

Крайний случай - ситуация, когда список **lists** пустой, тогда возвращаем **None**, или в нём один элемент, тогда мы возвращаем этот элемент (объединения одного списка).

Рекуррентный случай - будем делить список **lists** на **2** до тех пор, пока его длина не станет равной **1** (Крайний случай). После этого мы вызываем нашу функцию для левой части массива **lists** и для правой. В конце нам остается объединить полученные списки с помощью ранее реализованной процедуры, которая объединяет **2** списка.



Вообще наше решение не самое простое. Можно было пройтись по всем списка массива, поочередно добавляя их узлы в очередь с приоритетами. Затем из очереди с приоритетами очень легко получить отсортированную последовательность.



## **Оценка:**

Решение с очередью с приоритетами менее эффективно, потому что его сложность по времени **O**(**N** * **logN**), где **N** - общее количество элементов во всех списках (сложность **heap** **sort**), а по памяти мы бы затратили **O**(**N**) на хранение нашей кучи.

Наше же решение по времени будет **O**(**N** * **logK**), **K** - количество списков. Оценка идет из того, что мы пройдемся по всем элементам **N** ровно **logK** раз. По памяти мы затратим **O**(**logK**). Это расходы на стек вызовов функций.

## Код:
```python
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        n = len(lists) // 2
        left = self.mergeKLists(lists[:n])
        right = self.mergeKLists(lists[n:])
        return self.merge2Lists(left, right)

    def merge2Lists(self, first: ListNode, second: ListNode) -> ListNode:
        dummy = ListNode()
        cur = dummy
        while first and second:
            if first.val < second.val:
                cur.next = first
                first = first.next
            else:
                cur.next = second
                second = second.next
            cur = cur.next

        if first:
            cur.next = first
        if second:
            cur.next = second

        return dummy.next

```

<div align='center'><h3><a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/110.Construct%20Quad%20Tree'>⬅️ предыдущая задача</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/README.md'>Все задачи</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/112.Maximum%20Subarray'>следующая задача ➡️</a></h3></div>