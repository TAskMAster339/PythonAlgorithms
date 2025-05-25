# [**63) Remove Nth Node From End of List**](https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/)

## **Условие:**

Дан указатель на начало односвязного списка **head** и число **n**. Нужно удалить **n**-ный с конца узел из списка и вернуть **head**.

## **Идея:**

Два указателя. Один будет опережать второй на **n** позиций.

## **Реализация:**

Создадим быстрый указатель, который сразу сдвинем на **n** элементов вперед. Если он при этом стал равен **None**, значит мы дошли до конца списка, значит нам нужно удалить первый элемент. Для этого просто возвращаем **head**.**next**.

Иначе создадим медленный указатель и указатель на элемент перед ним **prev**. Теперь двигаем быстрый указатель до конца списка, параллельно двигая медленный и **prev**.

После окончания цикла обновляем **prev**.**next** = **prev**.**next**.**next**: убираем тот узел, на котором остановился медленный указатель.

В конце возвращаем **head**.



## **Оценка:**

По времени верхняя граница равняется **O**(**N**), один проход по списку длиной **N**, по памяти мы потратим **O**(**1**).

## Код:
```python
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(
        self, head: Optional[ListNode], n: int
    ) -> Optional[ListNode]:
        fast_pointer = head

        for i in range(n):
            fast_pointer = fast_pointer.next

        if not fast_pointer:
            return head.next

        slow_pointer = head
        prev = None

        while fast_pointer:
            fast_pointer = fast_pointer.next
            prev = slow_pointer
            slow_pointer = slow_pointer.next

        prev.next = prev.next.next

        return head

```

### [<-- предыдущая задача](https://github.com/TAskMAster339/PythonAlgorithms/tree/main/62.Reverse%20Nodes%20in%20k-Group) | [следующая задача -->](https://github.com/TAskMAster339/PythonAlgorithms/tree/main/64.Remove%20Duplicates%20from%20Sorted%20List%20II)
