# [**71) Symmetric Tree**](https://leetcode.com/problems/symmetric-tree/description/)

## **Условие:**

Дан корень бинарного дерева, нужно проверить является ли дерево зеркальным по отношению к самому себе (симметричным относительно своего центра)

## **Идея:**

Один **DFS** хорошо, но два еще лучше

## **Реализация:**

**Напишeм** вспомогательную функцию, которая будет принимать два узла **left_node** и **right_node**. Она будет рекурсивно проверять два поддерева на зеркальность.

Рассмотрим крайний случай: два узла равны **None**, возвращаем **True**, значит поддеревья зеркальны. Если только один из узлов **None**, то возвращаем **False**, это значит, что одно из поддеревьев больше другого, что говорит об их не зеркальности.

Рекуррентный случай будет следующим: проверяем равны ли значения в узлах **left_node** и **right_node**, также проверяем значения в их поддеревьях симметричным образом. Если у **left_node** взяли левое поддерево, то в сравнение с ним берем у **right_node** правое поддерево, и наоборот.



## **Оценка:**

Верхняя граница по времени будет **O**(**N**), где **N** - количество элементов в дереве. По памяти будет хорошо знакомый нам трап **O**(**1**).

## Код:
```python
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        return self.checkSymmetryOfSubTree(root.left, root.right)

    def checkSymmetryOfSubTree(
        self,
        left_node: Optional[TreeNode],
        right_node: Optional[TreeNode],
    ) -> bool:
        if not left_node and not right_node:
            return True

        if not left_node or not right_node:
            return False

        return (
            left_node.val == right_node.val
            and self.checkSymmetryOfSubTree(left_node.left, right_node.right)
            and self.checkSymmetryOfSubTree(left_node.right, right_node.left)
        )

```

### [<-- предыдущая задача](https://github.com/TAskMAster339/PythonAlgorithms/tree/main/70.Invert%20Binary%20Tree) | [следующая задача -->](https://github.com/TAskMAster339/PythonAlgorithms/tree/main/72.Construct%20Binary%20Tree%20from%20Preorder%20and%20Inorder%20Traversal)
