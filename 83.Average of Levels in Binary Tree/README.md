<div align='center'>
<h1><a href='https://leetcode.com/problems/average-of-levels-in-binary-tree/description/'><strong>83) Average of Levels in Binary Tree</strong></a></h1>
</div>

## **Условие:**

Дан корень **root** бинарного дерева, нужно вернуть массив средних значений узлов на каждом уровне

## **Идея:**

Такая же логика, как и в предыдущей задаче

## **Реализация:**

Реализуем предыдущий **BFS**, который за одну итерацию цикла **while** будет проходить по одному уровню дерева. При этом в начале итерации создадим **sum_of_level**, которую будем динамически обновлять во внутреннем цикле, и **num** - количество узлов, которые находяться в этом уровне. В конце итерации добавляем в массив среднее значение.



## **Оценка:**

Верхняя граница по времени снова будет **O**(**N**), где **N** - количество узлов в дереве. А верхняя граница по памяти будет **O**(**M**), где **M** = **2**^(**logN** - **1**) = **N** / **2**

## Код:
```python
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> list[float]:
        result = []

        queue = [root]

        while queue:
            sum_of_level = 0
            num = len(queue)

            for _ in range(len(queue)):
                node = queue.pop(0)
                if node:
                    sum_of_level += node.val
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            result.append(sum_of_level / num)
        return result

```

<div align='center'><h3><a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/82.Binary%20Tree%20Right%20Side%20View'>⬅️ предыдущая задача</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/README.md'>Все задачи</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/84.Binary%20Tree%20Level%20Order%20Traversal'>следующая задача ➡️</a></h3></div>