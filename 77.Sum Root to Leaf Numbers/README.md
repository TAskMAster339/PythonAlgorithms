# [**77) Sum Root to Leaf Numbers**](https://leetcode.com/problems/sum-root-to-leaf-numbers/description/)

## **Условие:**

Дан корень **root** бинарного дерева, содержащего только цифры от **0** до **9**. Каждый путь от корня до листа представляет число. Например путь **1**->**2**->**3** = **123**. Нужно вернуть сумму всех путей от корня до листа

## **Идея:**

Вспомнить экспоненциальную запись числа

## **Реализация:**

Реализуем функции, которая будет принимать узел **root** и число **num**. Если узел равен **None**, то возвращаем **0**. Затем рассчитываем число **num** = **10** * **num** + **root**.**val**. Затем если узел лист, то возвращаем число **num**. Иначе возвращаем сумму наших функций от левого и правого поддерева.



## **Оценка:**

Классический **DFS** имеет верхнюю границу по времени **O**(**N**), где **N** - количество узлов в дереве. По памяти стек рекурсии займет в наихудшем случае **O**(**N**).

## Код:
```python
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, 0)

    def dfs(self, root: Optional[TreeNode], num: int) -> int:
        if not root:
            return 0

        num = 10 * num + root.val
        if not root.left and not root.right:
            return num
        return self.dfs(root.left, num) + self.dfs(root.right, num)

```

### [<-- предыдущая задача](https://github.com/TAskMAster339/PythonAlgorithms/tree/main/76.Path%20Sum) | [следующая задача -->](https://github.com/TAskMAster339/PythonAlgorithms/tree/main/78.Binary%20Tree%20Maximum%20Path%20Sum)
