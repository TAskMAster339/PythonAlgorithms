# [**75) Flatten Binary Tree to Linked List**](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/)

## **Условие:**

Дан корень **root** бинарного дерева, нужно разгладить его в связный список. Связный список должен использовать тот же **TreeNode** класс, где правый ребенок **right** будет указывать на следующий элемент в списке, в то время как **left** всегда будет **None**. Порядок элементов в списке должен быть такой же как при прямом обходе дерева (**NLR**)

## **Идея:**

Всё что нужно сделать - поменять ссылки

## **Реализация:**

Идея будет в следующем. Мы должны взять наше левое поддерево и поставить его на место правого. При этом правое дерево нужно привязать к самому правому элементу левого поддерева. Повторяя эти действия, пока у дерева есть хотя бы одно левое поддерево.

Также стоит не забыть у всех узлов подправить **left** на **None**



## **Оценка:**

Алгоритм происходит за один цикл, где мы переберем все **N** узлов, поэтому верхняя граница по времени **O**(**N**), так как мы всего-напросто меняем ссылки, ничего при этом не сохраняя, поэтому оценка по памяти будет **O**(**1**)

## Код:
```python
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        left_node = root

        while left_node:
            if left_node.left:
                right_subtree = left_node.right
                left_node.right = left_node.left
                left_node.left = None
                left_node = left_node.right  # next left node

                join_node = left_node
                while join_node and join_node.right:
                    join_node = join_node.right

                join_node.right = right_subtree
            elif left_node.right:
                left_node = left_node.right
            else:
                break

        return root

```

