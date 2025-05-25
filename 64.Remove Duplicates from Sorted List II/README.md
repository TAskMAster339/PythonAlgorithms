# [**64) Remove Duplicates from Sorted List II**](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/)

## **Условие:**

Дан указатель на начало отсортированного односвязного списка **head**. Нужно удалить все узлы, в которых дублируются значения, оставив только уникальные числа в изначальном списке. Вернуть нужно тоже отсортированный список.

## **Идея:**

Нужно просто грамотно двигать три указателя.

## **Реализация:**

Во-первых, проверим, что список непустой или содержит более **1** узла. Если это не так, то просто возвращаем **head**.

Во-вторых, создаем три указателя: **left** = **start** - левый указатель, **right** = **start**.**next** - правый указатель и **prev** = **None** - указатель на узел перед **left**.

Теперь остаётся в цикле двигать указатели. Если **left**.**val** != **right**.**val**, то просто двигаем указатели. Иначе двигаем указатель **right** до тех пор, пока **left**.**val** == **right**.**val**. После этого, если **prev** **is** **not** **None**, то мы меняем ссылки:

**prev**.**next** = **right** и **left** = **prev**. Этим мы удалим все дубликаты между узлами **left** и **right**.

Если **prev** **is** **None**, то дубликаты нужно удалять от начала списка. В этом случае мы присваиваем **left** = **right**, **right** = **right**.**next**, **start** = **left**.

Цикл завершается как только **right** дошел до конца списка.

В конце возвращаем указатель **start**, который представляет собой отсортированный список **head** без дубликатов



## **Оценка:**

По времени мы затратим **O**(**N**), где **N** - длина списка. А по памяти **O**(**1**), так как создаем всего три ссылки.

## Код:
```python
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start = head
        if not start or start.next is None:
            return head

        left = start
        right = start.next
        prev = None

        while True:
            if left.val != right.val:
                prev = left
                left = right
                right = right.next
            else:
                while right and left.val == right.val:
                    right = right.next
                if prev:
                    prev.next = right
                    left = prev
                else:
                    left = right
                    if right:
                        right = right.next
                    start = left
            if not right:
                break
        return start

```

### [<-- предыдущая задача](https://github.com/TAskMAster339/PythonAlgorithms/tree/main/63.Remove%20Nth%20Node%20From%20End%20of%20List) | [следующая задача -->](https://github.com/TAskMAster339/PythonAlgorithms/tree/main/65.Rotate%20List)
