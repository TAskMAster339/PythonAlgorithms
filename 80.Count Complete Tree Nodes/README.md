<div align='center'>
<h1><a href='https://leetcode.com/problems/count-complete-tree-nodes/description/'><strong>80) Count Complete Tree Nodes</strong></a></h1>
</div>

## **Условие:**

Дан корень **root** заполненного бинарного дерева. Нужно вернуть количество узлов в дереве. Алгоритм должен быть быстрее, чем **O**(**N**).

Заполненное бинарное дерево - бинарное дерево, в котором на каждый уровень, кроме последнего, полностью заполнен, при этом узлы в последнем уровне располагаются слева настолько, насколько это возможно

## **Идея:**

Нужно загуглить про идеальное бинарное дерево

## **Реализация:**

Идеальное бинарное дерево - бинарное дерево, в котором есть все узлы имеют детей, кроме листьев, при этом все листья расположены на одном и том же уровне. Идеальное бинарное дерево всегда является заполненным, обратное не верно.

Если мы сможем доказать, что наше заполненное дерево - идеальное, то мы сможем посчитать количество его узлов по формуле **2**^**h** - **1**, где **h** - глубина дерева.

Для того, чтобы доказать, что наше заполненное дерево - идеальное, нужно проверить глубину до самого левого листа и глубину до самого правого листа.

Если они равны, то по определению заполненного дерева, мы делаем вывод, что самый последний уровень полный, следовательно, дерево - идеальное и количество узлов в нем равно **2**^**h** - **1**.

Иначе мы вызываем повторяем алгоритм рекурсивно для левого и правого поддеревьев. Возвращаем сумму их узлов + **1** (учитывая корень).



## **Оценка:**

Верхняя оценка по времени будет **O**(**log**^**2** **N**) (**O** (**logN** * **logN**)), так как расчет глубины в наихудшем случае будет **O**(**logN**), также в наихудшем случае нам потребуется рассчитать **logN** раз эту глубину.(Также очень хорошая оптимизация - замена **2**^**h** - **1** на **1** << **h** - **1**, где << - битовый сдвиг влево) По памяти мы затратим **O**(**logN**), так как в наихудшем случае размер стека рекурсии будет **logN**.

## Код:
```python
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left_depth = self.get_depth(root.left, is_left=True)
        right_depth = self.get_depth(root.right, is_left=False)

        if left_depth == right_depth:
            return (1 << left_depth) - 1  # <=> 2**left_depth - 1

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    def get_depth(
        self,
        node: Optional[TreeNode],
        *,
        is_left: bool = True,
    ) -> int:
        depth = 1
        while node:
            node = node.left if is_left else node.right
            depth += 1
        return depth

```

<div align='center'><h3><a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/79.Binary%20Search%20Tree%20Iterator'>⬅️ предыдущая задача</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/README.md'>Все задачи</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/81.Lowest%20Common%20Ancestor%20of%20a%20Binary%20Tree'>следующая задача ➡️</a></h3></div>