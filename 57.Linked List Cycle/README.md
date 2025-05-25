# [**57) Linked List Cycle**](https://leetcode.com/problems/linked-list-cycle/description/)

## **Условие:**

Дан указатель на начало связного списка **head**. Нужно определить есть ли в этом списке цикл. Если в списке есть цикл, нужно вернуть **True**, иначе **False**.

## **Идея:**

Два указателя.

## **Реализация:**

Создадим два указателя **fast** и **slow**, указывающих на **head**. Далее в цикле будем обновлять их значения. **slow** будет теперь указывать на следующий элемент. А **fast** на следующий после следующего. Иначе говоря, **fast** будет ровно в два раза быстрее **slow**, поэтому, если мы встретим какой-либо цикл указателем **slow**, то в этот момент **fast** уже пройдет его и станет равным **slow**. В этот момент возвращаем **True**.

Если мы до конца списка быстрым указателем, то возвращаем **False**.



## **Оценка:**

Верхняя граница по времени **O**(**N**), где **N** - длина списка. По памяти граница будет **O**(**1**).

## Код:
```python
from typing import Optional
from util import test_case


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True

        return False


if __name__ == "__main__":
    start = ListNode(3)
    second = ListNode(2)
    third = ListNode(0)
    fourth = ListNode(5)
    last = ListNode(-4)
    start.next = second
    second.next = third
    third.next = fourth
    fourth.next = last
    last.next = second

    uno_lst = ListNode(1)
    f = Solution().hasCycle
    test_case(f, True, start)
    test_case(f, False, uno_lst)

```

### [<-- предыдущая задача](https://github.com/TAskMAster339/PythonAlgorithms/tree/main/56.Basic%20Calculator) | [следующая задача -->](https://github.com/TAskMAster339/PythonAlgorithms/tree/main/58.Add%20Two%20Numbers)
