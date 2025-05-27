<div align='center'>
<h1><a href='https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/'><strong>85) Binary Tree Zigzag Level Order Traversal</strong></a></h1>
</div>

## **Условие:**

Дан корень **root** бинарного дерева, нужно вернуть зигзагообразный порядок обхода значений его узлов по уровням, слева направо, затем право налево для следующего уровня, затем слева направо и т.д.

## **Идея:**

Тот же самый **BFS**, только нужно умно его разворачивать

## **Реализация:**

Реализуем **BFS** по уровням. Каждую итерацию будем создавать массив **level** = [**0**] * **size**, где **size** = **len**(**queue**). Так же нам понадобиться булева переменная **right_to_left_flag** = **False**, которую мы будем менять от уровня к уровню.

Мы реализуем классический **BFS** слева направо, но в зависимости от булевой переменной мы будем добавлять значения узлов либо в начало массива, либо в конец. Таким образом каждый нечетный уровень будет в обычном порядке, а каждый нечетный в обратном порядке. Так появился он, Зигзагообразный обход.



## **Оценка:**

Верхняя оценка по времени будет **O**(**N**), где **N** - число узлов в дереве. По памяти граница будет **O**(**M**), где **M** = **N** / **2**.

## Код:
```python
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        if not root:
            return []
        result = []

        queue = [root]

        right_to_left_flag = False

        while queue:
            size = len(queue)
            level = [0] * size

            for i in range(len(queue)):
                node = queue.pop(0)
                if node:
                    index = size - 1 - i if right_to_left_flag else i
                    level[index] = node.val
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            result.append(level)
            right_to_left_flag = not right_to_left_flag
        return result

```

<div align='center'><h3><a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/84.Binary%20Tree%20Level%20Order%20Traversal'>⬅️ предыдущая задача</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/README.md'>Все задачи</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/86.Minimum%20Absolute%20Difference%20in%20BST'>следующая задача ➡️</a></h3></div>