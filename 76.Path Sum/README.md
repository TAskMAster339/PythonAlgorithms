# [**76) Path Sum**](https://leetcode.com/problems/path-sum/description/)

## **Условие:**

Дан корень **root** бинарного дерева и число **targetSum**, нужно вернуть **True**, если в дереве есть путь от корня до листа, в котором сумма значений **val** входящих в него узлов равна **targetSum**.

Лист - узел без детей.

## **Идея:**

**DFS**, **DFS**, **DFS**!!!

## **Реализация:**

Простая рекурсия. Сумма пути от корня до листа равна значению **val** корня плюс сумма пути от корня поддерева до листа.

Крайний случай если **root** это **None**, то возвращаем **False**. А если **root** это лист, то мы возвращаем **targetSum** == **root**.**val**.

А в рекуррентном случае мы будем вызывать нашу же функцию для левого и правого поддерева соответственно. При этом мы будем передавать в эти функции **targetSum** - **root**.**val**

В конце возвращаем логическое или результатов поиска суммы пути в поддеревьях.



## **Оценка:**

Классический **DFS** по времени займет у нас **O**(**N**), где **N** - количество узлов в дереве. При этом в среднем он может быть быстрее, так как логическое или в **Python** ленивое, то есть есть вероятность, что мы найдем путь где-то в начале, тогда все оставшиеся пути вычислены не будут. По памяти мы потратим **O**(**N**), необходимый для рекурсии стек.

## Код:
```python
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return targetSum == root.val
        return self.hasPathSum(
            root.left,
            targetSum - root.val,
        ) or self.hasPathSum(
            root.right,
            targetSum - root.val,
        )

```

### [<-- предыдущая задача](https://github.com/TAskMAster339/PythonAlgorithms/tree/main/75.Flatten%20Binary%20Tree%20to%20Linked%20List) | [следующая задача -->](https://github.com/TAskMAster339/PythonAlgorithms/tree/main/77.Sum%20Root%20to%20Leaf%20Numbers)
