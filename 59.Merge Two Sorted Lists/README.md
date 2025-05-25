# [**59) Merge Two Sorted Lists**](https://leetcode.com/problems/merge-two-sorted-lists/description/)

## **Условие:**

Даны два указателя на начало двух отсортированных связных списков **list1** и **list2**. Нужно объединить эти два списка в один отсортированный.

## **Идея:**

Как будто массивы, только с указателями нужно не запутаться

## **Реализация:**

Создаем новый список. Затем пока в хотя бы одном списке есть число, мы берем это число, если список закончился, будем брать -**inf**. Затем сравниваем два числа. Если первое меньше, то добавляем его в наш список, двигая указаетель первого данного списка. Если второе, то его добавляем и двигаем указатель второго списка.

В конце аналогично предыдущей задачи возвращаем указатель на начало нашего списка.



## **Оценка:**

По времени мы затратим **O**(**N** + **K**), где **N**, **K** - длины списков. По памяти мы потратим **O**(**N** + **K**).

## Код:
```python
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        newList = ListNode(0)
        begin = newList

        while list1 or list2:
            val1 = list1.val if list1 else float("inf")
            val2 = list2.val if list2 else float("inf")

            if val1 < val2:
                newList.next = ListNode(val1)
                list1 = list1.next if list1 else None
            elif val2 <= val1:
                newList.next = ListNode(val2)
                list2 = list2.next if list2 else None
            newList = newList.next

        result = begin.next
        begin.next = None
        begin = None
        return result


if __name__ == "__main__":
    list1 = ListNode(1, ListNode(2, ListNode(4)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))

    f = Solution().mergeTwoLists(list1, list2)
    while f:
        print(f.val)
        f = f.next

```

### [<-- предыдущая задача](https://github.com/TAskMAster339/PythonAlgorithms/tree/main/58.Add%20Two%20Numbers) | [следующая задача -->](https://github.com/TAskMAster339/PythonAlgorithms/tree/main/60.Copy%20List%20with%20Random%20Pointer)
