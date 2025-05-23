# [**65) Rotate List**](https://leetcode.com/problems/rotate-list/description/)

## **Условие:**

Дан указатель на начало односвязного списка **head**. Нужно циклически сдвинуть элементы вправо на **k** мест.

## **Идея:**

Вспомнить, что такое циклический сдвиг.

## **Реализация:**

Так как **k** может быть очень большим, а длина списка очень маленькой, то нам очень хочется разделить **k** по модуля на длину списка. Еще нам понадобятся три указателя. Один на новое начало списка, другой на предыдущий элемент перед новым началом, третий на конец текущего списка.

Сначала, посчитаем длину списка и также найдем его конец. После простой итерации у нас есть **length** и **end** - указатель на последний узел.

Делим **k** по модулю. И если **k** оказалось равным **0**, то возвращаем **head**, так как список двигать не нужно.

Иначе создаем оставшиеся два указателя **start** и **prev**. И в цикле, в котором **length** - **k** итераций, их вычисляем.

В конце меняем ссылки: **prev**.**next** = **None**, **end**.**next** = **head**.

Возвращаем наш указатель **start**.



## **Оценка:**

По времени мы затратим **O**(**N**), в этой границе скрыта константа **2**, так как мы делаем два пробега по циклу. По памяти мы затратим **O**(**1**).

## Код:
```python
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(
        self,
        head: Optional[ListNode],
        k: int,
    ) -> Optional[ListNode]:
        end = head
        length = 1
        if not end or not end.next:
            return head

        while end.next:
            end = end.next
            length += 1

        k %= length

        if k == 0:
            return head

        start = head
        prev = None

        for i in range(length - k):
            prev = start
            start = start.next

        prev.next = None
        end.next = head
        return start

```

