<div align='center'>
<h1><a href='https://leetcode.com/problems/copy-list-with-random-pointer/description/'><strong>60) Copy List with Random Pointer</strong></a></h1>
</div>

## **Условие:**

Дан связный список длинной **n**, каждый узел содержит указатель на какой-то случайный узел в списке. Нужно сделать глубокую копию списка. (В новом списке не должно быть ничего, что могло бы ссылаться на предыдущий).

## **Идея:**

Надо постепенно копировать объекты.

## **Реализация:**

Я нашел следующие решение. Его легко понять, но сложно реализовать.

Во-первых, сделаем копии каждому узлу в данном списке и расположим их пряма за оригиналом. (**1**->**2**->**3**  ==>  **1**->**1**->**2**->**2**->**3**->**3**)

Во-вторых, пройдемся теперь по созданным нами копиям, они будут по четным индексам списка. Наша задача скопировать рандомные указатели. Логика следующая. Для **i**-того узла находим рандомный указатель **i**-**1** узла. И двигаем этот указатель на следующий элемент (Следующий за ним будет его копией, которую мы создали раньше). Присваиваем **i**-тому узлу этот указатель в поле **random**.

В-третьих, нужно разделить список. Сейчас у нас один большой список, где по нечетным индексам расположены элементы изначального списка, а по четным созданные нами глубокие копии соответствующих элементов. Этого достаточно, чтобы разделить список на два, на изначальный и на его копию. После разделения остается вернуть указатель на начало копии списка.



## **Оценка:**

Всего у нас будет три цикла, первый по времени займет **O**(**N**), второй **O**(**2N**), третий **O**(**2N**), где **N** - длина списка. Итого верхняя граница по времени равна **O**(**N**). По памяти мы затратим **O**(**N**) (потому что копируем).

## Код:
```python
from typing import Optional


class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if not head:
            return None

        # Copy of all Nodes
        curr = head
        while curr:
            new_node = Node(curr.val, curr.next)
            curr.next = new_node
            curr = new_node.next

        curr = head
        # make new Random nodes connections
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        old_head = head
        new_head = head.next
        curr_old = old_head
        curr_new = new_head

        # Slice two lists
        while curr_old:
            curr_old.next = curr_old.next.next
            curr_new.next = curr_new.next.next if curr_new.next else None
            curr_old = curr_old.next
            curr_new = curr_new.next

        return new_head

```

<div align='center'><h3><a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/59.Merge%20Two%20Sorted%20Lists'>⬅️ предыдущая задача</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/README.md'>Все задачи</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/61.Reverse%20Linked%20List%20II'>следующая задача ➡️</a></h3></div>