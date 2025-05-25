<div align='center'>
<h1><a href='https://leetcode.com/problems/partition-list/description/'><strong>66) Partition List</strong></a></h1>
</div>

## **Условие:**

Дан указатель на начало односвязного списка **head** и значение **x**, нужно разбить список так, чтобы все узлы, значение которых меньше **x**, были в списке раньше всех узлов, значение которых больше или равно **x**.

При этом нужно сохранить исходный порядок узлов в списке.

## **Идея:**

Бинарное дерево.

## **Реализация:**

Создадим две болванки **less** и **more**, к которым мы будем приклеивать узлы, которые меньше или больше, чем **x**. Затем в цикле мы проходим по всем узлам, создаем их копии и присоединяем их к соответствующим спискам. (Можно не создавать копии, но при этом нужно будет учесть, что может возникнуть ссылка на саму себя). Затем остается грамотно объединить полученные списки в один и вернуть его. Так как эти списки были получены одним прямым проходом по исходному списку, то мы можем гарантировать, что порядок элементов будет сохранён.



## **Оценка:**

По времени мы затратим **O**(**N**), так как проходим по списку длинной **N**. По памяти мы затратим **O**(**N**), так как создаем копию каждого узла. Можно сократить до **O**(**1**), если разобраться с ссылками. Но я выбрал копирование, так как это гарантирует, что мы получаем новый уникальный объект. (Его нельзя будет менять с помощью изначального списка, что очень надежно).

## Код:
```python
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(
        self,
        head: Optional[ListNode],
        x: int,
    ) -> Optional[ListNode]:
        less = ListNode()
        more = ListNode()

        start = less
        end = more

        while head:
            if head.val < x:
                less.next = ListNode(head.val)
                less = less.next
            else:
                more.next = ListNode(head.val)
                more = more.next
            head = head.next

        less.next = end.next
        return start.next

```

<div align='center'><h3><a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/65.Rotate%20List'>⬅️ предыдущая задача</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/README.md'>Все задачи</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/67.LRU%20Cache'>следующая задача ➡️</a></h3></div>