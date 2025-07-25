<div align='center'>
<h1><a href='https://leetcode.com/problems/sort-list/description/'><strong>109) Sort List</strong></a></h1>
</div>

## **Условие:**

Дан указатель **head** на связный список, нужно вернуть лист отсортированный в возрастающем порядке

## **Идея:**

Реализовать **merge** **sort** для списка

## **Реализация:**

Идея сортировки слиянием состоит в том, чтобы делить массив пополам до тех пор, пока мы не получим единичные отсортированные массива, которые потом будут объединены вместе.

В списке у нас нет индексов. Для того, чтобы найти середину необходимо создать два указателя: **slow** и **fast**. **Fast** будет идти в два раза быстрее **slow**. Это значит, что если **fast** дойдет до конца списка, то **slow** будет указывать на середину.

Остается разделить исходный список на два и рекурсивно вызвать сортировку слиянием для левой части и правой.

В конце мы должны вернуть слияние двух списков.



## **Оценка:**

Верхняя граница по времени будет **O**(**N** * **logN**), это сложность сортировки слиянием.

Верхняя граница по памяти будет **O**(**logN**), это расходы на стек вызовов функции.

## Код:
```python
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        prev, slow, fast = None, head, head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = None
        left = self.sortList(head)
        right = self.sortList(slow)

        return self.merge(left, right)

    def merge(self, left: ListNode, right: ListNode) -> ListNode:
        dummy = ListNode()
        curr = dummy
        while left and right:
            if left.val > right.val:
                curr.next = right
                right = right.next
            else:
                curr.next = left
                left = left.next
            curr = curr.next

        if left:
            curr.next = left
        if right:
            curr.next = right

        return dummy.next

```

<div align='center'><h3><a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/108.Convert%20Sorted%20Array%20to%20Binary%20Search%20Tree'>⬅️ предыдущая задача</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/README.md'>Все задачи</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/110.Construct%20Quad%20Tree'>следующая задача ➡️</a></h3></div>