<div align='center'>
<h1><a href='https://leetcode.com/problems/invert-binary-tree/description/'><strong>70) Invert Binary Tree</strong></a></h1>
</div>

## **Условие:**

Дан корень бинарного дерева, нужно инвертировать дерево и вернуть его корень

## **Идея:**

Я до этой задачи не понимал насколько **DFS** крут

## **Реализация:**

Спускаемся сверху вниз с помощью рекурсии. Крайним случаем будет узел, который равен **None**, тогда возвращаем **None**. Рекуррентный случай - меняем левого и правого ребенка родительского узла. (с помощью ведерка). Затем делаем ту же операцию сначала для левого, потом для правого ребенка.



## **Оценка:**

По времени верхняя граница будет **O**(**N**), где **N** - количество узлов в дереве. По памяти **O**(**1**), но, вы, помните, что она с приколом.

## Код:
```python
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        tmp_node = root.left
        root.left = root.right
        root.right = tmp_node

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

```

<div align='center'><h3><a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/69.Same%20Tree'>⬅️ предыдущая задача</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/README.md'>Все задачи</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/71.Symmetric%20Tree'>следующая задача ➡️</a></h3></div>