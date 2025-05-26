<div align='center'>
<h1><a href='https://leetcode.com/problems/binary-tree-right-side-view/description/'><strong>82) Binary Tree Right Side View</strong></a></h1>
</div>

## **Условие:**

Дан корень **root** бинарного дерева, представьте себе, что вы стоите справа от дерева и смотрите прямо. Нужно вернуть все значения узлов, которые вы видете сверху вниз

## **Идея:**

Нужно просто вернуть список самых правых узлов в каждом уровне дерева

## **Реализация:**

Создадим массив **result**, в которой будем записывать наши значения. Далее реализуем **BFS**, создадим очередь, в которую добавим **root**.

Теперь будем обрабатывать уровни дерева, для этого внутри цикла **while** **queue** добавим цикл **for**, который будет пробегаться по всем элементам в очереди. Таким образом мы будем обрабатывать по уровню дерева за одну итерацию цикла **while**.

Остается создать переменную **right_side_view**, в которую будем динамически записывать обрабатываемый узел в цикле **for**. Тогда после его окончания в переменной будет записан самый правый узел, находящийся на этом уровне. Его мы заносим в **result**.



## **Оценка:**

Верхняя граница по времени у **BFS** будет **O**(**N**), где **N** - количество узлов в дереве. По памяти мы затратим **O**(**N**), так как в наихудшем случае нам потребуется сохранить все **N** узлов.

## Код:
```python
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        result = []

        queue = [root]

        while queue:
            right_side_view = None

            for _ in range(len(queue)):
                node = queue.pop(0)
                if node:
                    right_side_view = node
                    queue.append(node.left)
                    queue.append(node.right)
            if right_side_view:
                result.append(right_side_view.val)
        return result

```

<div align='center'><h3><a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/81.Lowest%20Common%20Ancestor%20of%20a%20Binary%20Tree'>⬅️ предыдущая задача</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/README.md'>Все задачи</a></h3></div>