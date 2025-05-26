<div align='center'>
<h1><a href='https://leetcode.com/problems/binary-tree-level-order-traversal/description/'><strong>84) Binary Tree Level Order Traversal</strong></a></h1>
</div>

## **Условие:**

Дан корень **root** бинарного дерева. Нужно вернуть обход значений узлов в порядке уровней, слева направо, уровень за уровнем.

## **Идея:**

Старый добрый **BFS**

## **Реализация:**

Реализуем тот же самый **BFS** по уровням. Только теперь каждую итерацию будем создавать массив **level**, в который будем заносить значения узлов в уровне. В конце итерации добавляем посчитанный массив в **result**. Его мы в конце возвращаем.



## **Оценка:**

Верхняя граница по времени у **BFS**, как мы уже знаем, **O**(**N**), где **N** - количество узлов. По памяти мы опять затратим **O**(**M**), где **M** - максимальная ширина бинарного дерева. **M** = **2**^(**logN** - **1**) = **N** / **2**. (Округляем до верха)

## Код:
```python
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        result = []

        queue = [root]

        while queue:
            level = []

            for _ in range(len(queue)):
                node = queue.pop(0)
                if node:
                    level.append(node)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)

            result.append(level)
        return result

```

<div align='center'><h3><a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/83.Average%20of%20Levels%20in%20Binary%20Tree'>⬅️ предыдущая задача</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/README.md'>Все задачи</a></h3></div>