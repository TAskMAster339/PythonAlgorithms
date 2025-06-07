<div align='center'>
<h1><a href='https://leetcode.com/problems/validate-binary-search-tree/description/'><strong>88) Validate Binary Search Tree</strong></a></h1>
</div>

## **Условие:**

Дан корень **root** бинарного дерева, нужно определить является ли оно бинарным деревом поиска **BST**

Бинарное дерево поиска обладает следующими свойствами:

**1**. Левое поддерево содержит только узлы со значениями меньшими, чем значение корня.

**2**. Правое поддерево содержит только узлы со значениями большими, чем значение корня

**3**. И левое и правое поддеревья являются тоже бинарными деревьями поиска.

## **Идея:**

Можно написать крутой **DFS** с верхней и нижней границами, но я просто пойду по **LNR**

## **Реализация:**

Мы будем идти по дереву с помощью центрированного обхода **DFS** **LNR**. При таком обходе только **BST** даст нам возрастающую последовательность чисел. Чтобы проверить её, будем запоминать предыдущие число и сравнивать его с текущим. Если текущие оказалось меньше или равно предыдущему, то возвращаем **False**. (Удобно создать флаг (из-за не очень хорошо работающего **return** в рекурсии), который будем поднимать и затем же с помощью него оптимизировать лишние рекурсии)



## **Оценка:**

Классическая оценка **DFS** по времени **O**(**N**), по памяти **O**(**N**), где **N** - количество узлов в дереве.

## Код:
```python
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        flag = True
        prev_node = None

        def dfs(node: Optional[TreeNode]) -> None:
            nonlocal flag, prev_node

            if not flag:
                return
            if node:
                dfs(node.left)
                if prev_node:
                    flag = prev_node.val > node.val
                prev_node = node
                dfs(node.right)

        dfs(root)
        return flag

```

<div align='center'><h3><a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/87.Kth%20Smallest%20Element%20in%20a%20BST'>⬅️ предыдущая задача</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/README.md'>Все задачи</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/89.Number%20of%20Islands'>следующая задача ➡️</a></h3></div>
