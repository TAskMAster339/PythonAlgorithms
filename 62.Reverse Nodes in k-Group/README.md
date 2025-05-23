# [**62) Reverse Nodes in k-Group**](https://leetcode.com/problems/reverse-nodes-in-k-group/description/)

## **Условие:**

Дан указатель **head** на начало односвязного списка. Нужно инвертировать группы, состоящие из **k** узлов.

Нужно инвертировать именно узлы, а не их значения.

## **Идея:**

Инверсия как в предыдущей задачи, только теперь это нужно будет сделать **k** раз

## **Реализация:**

Напишем вспомогательную функцию **reverse**(**start**, **end**), с помощью которой будем инвертировать список. (Смотри задачу **61**)

Далее самый простой способ делать это рекурсией. Найдем узел, который находится на расстаянии **k** от начала списка **head**. Если такого нет, возвращаем **head**. Это наш крайний случай.

Рекурентный случай будет таковым: вызываем **reverse**, который инвертирует нам первую группу, сохраняем указатель, который он вернет, потому что это будет начало списка, который мы в итоге вернем. Затем в **head**.**next** записываем **reverseGroup**, но уже для следующей группы. Это присваивание нужно для того, чтобы связать инвертированные списки воедино.



## **Оценка:**

По времени мы затратим **O**(**N**), так как мы делаем это всего за один проход по списку длиной **N**. По памяти **O**(**1**).

## Код:
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverse(self, start, end):
        prev, curr = None, start
        while curr != end:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

    def reverseKGroup(self, head, k):
        count, temp = 0, head
        while temp and count < k:
            temp = temp.next
            count += 1
        if count < k:
            return head

        new_head = self.reverse(head, temp)
        head.next = self.reverseKGroup(temp, k)
        return new_head

```

