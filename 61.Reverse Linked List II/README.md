<div align='center'>
<h1><a href='https://leetcode.com/problems/reverse-linked-list-ii/description/'><strong>61) Reverse Linked List II</strong></a></h1>
</div>

## **Условие:**

Дан односвязный список **head** и два числа **left** и **right**, где **left** <= **right**. Нужно инвертировать узлы, которые расположены между узлами под номерами **left** и **right**. Нумерация начинается с **1**.

## **Идея:**

Инверсия в односвязном списке это просто инверсия связей. Смотри рисунок.

## **Реализация:**

Опять идея очень элементарная, но реализовать очень сложно.

Создаем указатель **LeftPointer** и **current**. Первый указывает на **left** - **1** элемент списка. **current** мы будем динамически двигать до **right**.

Теперь мы замутим следующий прикол:

Для примера возьмем список **1**->**2**->**3**->**4**->**5** и **left**=**2**, **right**=**4**. Мы должны сделать **1**->**4**->**3**->**2**->**5**

Рассмотрим связь **2**->**3**. Нам нужно её инвертировать, то есть получить **2**<-**3**. Для этого мы разорвем эту связь, но при этом сохраним указатель на **3** в **nextNodePointer**, потому что иначе мы потеряем этот объект (у нас не будет ни одной ссылки, указывающий на него, а сборщик мусора такое не прощает). Указатель на **2** у нас храниться в **current**. Остается присвоить **current** = **prevPointer**, который в первый раз будет **None**. После данной операции двигаем **current** на **nextNodePointer**. И обновляем **prevPointer**. Сейчас пойдет магия.

В итоге мы получим **1**->**2** **3**->**4**->**5**

Повторим этот алгоритм для **current**=**3**, **prevNode**=**2**

Получим **1**->**2**<-**3** **4**->**5**. Продолжим магию.

Еще раз: **1**->**2**<-**3**<-**4**->**5**. Поздравляю мы инвертировали элементы с позиции **left** до **right**. Для того, чтобы получить правильный ответ, нужно изменить указатель у **left** - **1** узла (**1** в данном примере), и указатель у **right** (**4** в данном примере). (**2** должна ссылаться на **current**==**5**, а **1** ссылаться на **prevPointer**==**4**)

Получим **1**->**4**->**3**->**2**->**5**



## **Оценка:**

Всего будет сделано **right** - **left** действий. Значит в наихудшем случае **right**=**N**, **left**=**0** где **N** - длина списка. Получим верхнюю границу в **O**(**N**). По памяти мы потратим **O**(**1**). Так как инвертируем на месте.

## Код:
```python
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        if not head and left == right:
            return head

        result = ListNode(0, head)
        LeftPointer, current = result, head

        for i in range(left - 1):
            LeftPointer, current = current, current.next

        prevPointer = None
        for i in range(right - left + 1):
            nextNodePointer = current.next
            current.next = prevPointer
            prevPointer, current = current, nextNodePointer

        LeftPointer.next.next = current
        LeftPointer.next = prevPointer
        return result.next

```

<div align='center'><h3><a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/60.Copy%20List%20with%20Random%20Pointer'>⬅️ предыдущая задача</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/README.md'>Все задачи</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/62.Reverse%20Nodes%20in%20k-Group'>следующая задача ➡️</a></h3></div>