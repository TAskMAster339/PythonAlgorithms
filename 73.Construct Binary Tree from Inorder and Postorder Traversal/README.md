<div align='center'>
<h1><a href='https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/'><strong>73) Construct Binary Tree from Inorder and Postorder Traversal</strong></a></h1>
</div>

## **Условие:**

Даны два массива целых чисел **inorder** и **postorder**, где **postorder** это обратный обход бинарного дерева (**LRN** **left**-**right**-**node**), а **inorder** это центрированный обход дерева (**LNR** **left**-**node**-**right**). Это обходы одного и того же дерева, нужно сконструировать его и вернуть

## **Идея:**

Смотри предыдущую задачу

## **Реализация:**

Та же самая идея только теперь у нас вместо прямого обхода дерева есть его обратный обход. Мы будем делать то же самое. Заметим, что последний элемент в **postorder** - корень дерева. Мы будем последовательно извлекать элементы с конца списка. Эти узлы мы будем с помощью списка **inorder** прикреплять к дереву. Важно, что мы в начале собираем правое поддерево, только потом левое, так как наш обход обратный.



## **Оценка:**

Сложность по времени будет **O**(**N**), где **N** - количество узлов в дереве. По памяти **O**(**N**), расходы на хэш-таблицу. :)

## Код:
```python
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(
        self,
        inorder: list[int],
        postorder: list[int],
    ) -> Optional[TreeNode]:
        table = {}

        for i in range(len(inorder)):
            table[inorder[i]] = i

        def build(start: int, end: int) -> Optional[TreeNode]:
            if start > end:
                return None
            root_value = postorder.pop()
            root = TreeNode(root_value)

            middle_index = table[root_value]
            root.right = build(middle_index + 1, end)
            root.left = build(start, middle_index - 1)

            return root

        return build(0, len(postorder) - 1)

```

<div align='center'><h3><a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/72.Construct%20Binary%20Tree%20from%20Preorder%20and%20Inorder%20Traversal'>⬅️ предыдущая задача</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/README.md'>Все задачи</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/74.Populating%20Next%20Right%20Pointers%20in%20Each%20Node%20II'>следующая задача ➡️</a></h3></div>