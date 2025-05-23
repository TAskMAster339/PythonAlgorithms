# [**58) Add Two Numbers**](https://leetcode.com/problems/add-two-numbers/description/)

## **Условие:**

Дано два непустых связных списка, которое представляют собой два натуральных числа. Цифры хранятся в обратном порядке и каждый узел содержит ровно одну цифру. Нужно сложить эти два числа и вернуть сумму в виде связного списка.

## **Идея:**

Вспомнить как складываются числа столбиком.

## **Реализация:**

Создадим новый список, который вернем. Не забываем сохранить указатель на его начало. (Это необходимо так как мы работаем с односвязным списком, мы просто не имеем возможности вернуться назад) Также нам потребуется переменная **carry** для хранения переноса.

Пока у нас есть числа в списках и **carry** != **0**, получаем цифры из списков. Вычисляем их сумму и перенос. Добавляем в наш новый список сумму.

После цикла возвращаем ранее сохраненный указатель на начало нашего списка.



## **Оценка:**

По времени **O**(**N** + **K**), где **N**, **K** - длины списков. По памяти **O**(**max**(**N**, **K**))

## Код:
```python
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        returnList = ListNode(0)
        begin = returnList
        carry = 0

        while l1 or l2 or carry != 0:
            digit1 = l1.val if l1 else 0
            digit2 = l2.val if l2 else 0

            total = (digit1 + digit2 + carry) % 10
            carry = (digit1 + digit2 + carry) // 10

            newNode = ListNode(total)
            returnList.next = newNode
            returnList = returnList.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        result = begin.next
        begin.next = None
        begin = None
        return result


if __name__ == "__main__":
    first = ListNode(2)
    first2 = ListNode(4)
    first3 = ListNode(3)
    first.next = first2
    first2.next = first3

    second = ListNode(5)
    second2 = ListNode(6)
    second3 = ListNode(4)
    second.next = second2
    second2.next = second3

    f = Solution().addTwoNumbers(first, second)

    while f:
        print(f.val)
        f = f.next

```

