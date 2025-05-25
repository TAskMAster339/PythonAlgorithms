# [**68) Maximum Depth of Binary Tree**](https://leetcode.com/problems/maximum-depth-of-binary-tree/description/)

## **Условие:**

Дан корень бинарного дерево нужно найти его максимальную глубину. Максимальная глубина - количество узлов на пути от корня к самому удаленному листу

## **Идея:**

Реализовать **DFS**

## **Реализация:**

Создадим вспомогательную функцию, которая рекурсивно будет вычислять глубину. Она будет принимать в себя узел и его текущую глубину в качестве аргументов. Если узел равен **None** или узел является листом, то возвращаем глубину, это будет наш крайний случай. В рекуррентном случае мы возвращаем максимум из глубины левого поддерева плюс один и глубины правого поддерева плюс один.

Осталось просто вызывать эту функции от корня с глубиной равной **1**



## **Оценка:**

По времени мы затратим **O**(**N**), где **N** - количество узлов в дереве. По памяти мы затратим **O**(**1**), потому что ничего никуда не сохраняем, но стоит помнить, что здесь скрыто потенциальное **O**(**N**), так как рекурсия в наихудшем случае потребует стек с размером **N**.

## Код:
```python
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return self.maxDepthRecursive(root, 1)

    def maxDepthRecursive(self, node: Optional[TreeNode], depth: int) -> int:
        if not node:
            return depth

        if not node.left and not node.right:
            return depth

        leftSubTreeDepth = self.maxDepthRecursive(node.left, depth + 1)
        rightSubTreeDepth = self.maxDepthRecursive(node.right, depth + 1)

        return max(leftSubTreeDepth, rightSubTreeDepth)

```

### [<-- предыдущая задача](https://github.com/TAskMAster339/PythonAlgorithms/tree/main/67.LRU%20Cache) | [следующая задача -->](https://github.com/TAskMAster339/PythonAlgorithms/tree/main/69.Same%20Tree)
