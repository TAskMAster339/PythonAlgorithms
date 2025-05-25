# [**81) Lowest Common Ancestor of a Binary Tree**](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/)

## **Условие:**

Дан корень бинарного дерева **root** и два узла **p** и **q**. Нужно найти наименьшего общего предка этих узлов.

Наименьший общий предок определяется между двумя узлами **p** и **q** как наименьший узел в дереве, который имеет как **p**, так и **q** в качестве потомков. При этом узел может быть потомком самого себя

## **Идея:**

Нету ничего лучше старого, доброго **DFS**

## **Реализация:**

Определим крайний случай: если узел **root** равен **None**, то возвращаем **None**. Если узел **root** равен узлу **p** или узлу **q**, то возвращаем **root**. (Случай, когда узел сам себе потомок)

Рекуррентный случай: вызываем нашу функцию для левого и правого поддеревьев **root**. Далее нужно рассмотреть возможные результаты.

Если оба результата не **None**, то мы получили случай, когда один из узлов **p** или **q**, находится в левом поддереве, в то время как второй в правом поддереве. Значит их наименьший общий предок - корень возвращаем **root**.

Если один из результатов вернул **None**, значит второй является наименьшим общим предком. Его мы возвращаем.



## **Оценка:**

По времени верхней границей будет **O**(**N**), так как **DFS** пройдет по всем узлам в дереве, которых **N** штук. По памяти мы затратим **O**(**N**) на стек рекурсии.

## Код:
```python
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self,
        root: "TreeNode",
        p: "TreeNode",
        q: "TreeNode",
    ) -> "TreeNode":
        if not root or root in {p, q}:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root

        return left or right

```

### [<-- предыдущая задача](https://github.com/TAskMAster339/PythonAlgorithms/tree/main/80.Count%20Complete%20Tree%20Nodes)