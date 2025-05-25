# [**69) Same Tree**](https://leetcode.com/problems/same-tree/description/)

## **Условие:**

Даны два корня бинарных деревьев **p** и **q**. Нужно реализовать функцию, которая проверяет одинаковы ли они или нет. Одинаковыми деревья считаются, если они имеют идентичную структуру и все соответствующие узлы имеют одинаковые значения

## **Идея:**

Тот же **DFS** только теперь будем проверять идентичность

## **Реализация:**

Пойдем также рекурсией. Для начала определим рекуррентный случай: бинарные деревья равные, если их левые и правые поддеревья равны.

Если значения узлов **p** и **q** не равны, возвращаем **False**, иначе возвращаем логическое И вызовов нашей функции для левого и правого поддеревьев **p** и **q** соответственно.

Теперь становиться очевидным крайний случай: если два узла **p** и **q** являются **None**, значит мы дошли до одного из листьев дерева, при этом не встретив разные значения в узлах, значит эта цепь узлов одинаковая у деревьев, можно возвращать **True**.

Если один из узлов **p** или **q** является **None**, то мы нашли несоответствие в цепи узлов, значит одно дерево длиннее другого, возвращаем **False**.



## **Оценка:**

По времени асимптотическая сложность равна **O**(**N**), где **N** - количество узлов, так как нам всегда нужно будет пройти все **N** узлов. По памяти **O**(**1**), но не забываем про стек рекурсии (см. **68** задачу)



## Код:
```python
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (not p and q) or (not q and p):
            return False
        if not q and not p:
            return True
        if p.val != q.val:
            return False
        isSameLeft = self.isSameTree(p.left, q.left)
        isSameRight = self.isSameTree(p.right, q.right)
        return isSameLeft and isSameRight

```

### [<-- предыдущая задача](https://github.com/TAskMAster339/PythonAlgorithms/tree/main/68.Maximum%20Depth%20of%20Binary%20Tree) | [следующая задача -->](https://github.com/TAskMAster339/PythonAlgorithms/tree/main/70.Invert%20Binary%20Tree)
