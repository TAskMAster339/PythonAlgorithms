<div align='center'>
<h1><a href='https://leetcode.com/problems/minimum-absolute-difference-in-bst/description/'><strong>86) Minimum Absolute Difference in BST</strong></a></h1>
</div>

## **Условие:**

Дан корень **root** бинарного дерева поиска **BST**, нужно вернуть минимальную абсолютную разность между значений между любыми двумя узлами

## **Идея:**

Нужно как-то сократить "любые два узла" до "вот этих двух узлов"

## **Реализация:**

На самом деле всё очень просто. Нужно пройтись по дереву с помощью **DFS** **LNR** (центрированным обходом).

Центрированный обход по **BST** представляет собой последовательность чисел, отсортированную в возрастающем порядке.

Рассмотрим три числа **a**, **b**, **c**, где **a** < **b** < **c**. Тогда минимальной абсолютной разностью может быть только **b**-**a** или **c**-**b**. Другие разности не подходят, так как **c**-**a** > **c**-**b** и **c**-**a** > **b**-**a** (это следует из условия нашей мини задачи).

Поэтому нам остается при обходе **LNR** динамически обновлять минимальную разность между текущим узлом и предыдущим.



## **Оценка:**

**DFS** имеет верхнюю границу по времени **O**(**N**), где **N** - количество узлов в дереве. По памяти мы затратим **O**(**N**), потому что стек рекурсии в наихудшем случае будет заполнен **N** элементами.

## Код:
```python
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        min_diff = float("inf")
        prev_node = None

        def dfs(node: Optional[TreeNode]) -> None:
            nonlocal min_diff, prev_node
            if node:
                dfs(node.left)
                if prev_node:
                    min_diff = min(min_diff, node.val - prev_node.val)
                prev_node = node
                dfs(node.right)

        dfs(root)
        return min_diff

```

<div align='center'><h3><a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/85.Binary%20Tree%20Zigzag%20Level%20Order%20Traversal'>⬅️ предыдущая задача</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/README.md'>Все задачи</a></h3></div>