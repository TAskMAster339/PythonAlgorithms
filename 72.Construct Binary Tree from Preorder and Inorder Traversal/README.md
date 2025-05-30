<div align='center'>
<h1><a href='https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/'><strong>72) Construct Binary Tree from Preorder and Inorder Traversal</strong></a></h1>
</div>

## **Условие:**

Даны два массива целых чисел **preorder** и **inorder**, где **preorder** это прямой обход бинарного дерева (**NLR** **node**-**left**-**right**), а **inorder** это центрированный обход дерева (**LNR** **left**-**node**-**right**). Это обходы одного и того же дерева, нужно сконструировать его и вернуть

## **Идея:**

Как-то связать два подвида **DFS**

## **Реализация:**

Для начала хорошо понять, что первый элемент в **preorder** - корень. Теперь наша задача построить его левое и правое поддеревья. Для этого нужно понять какие узлы находятся по правую его сторону, а какие по левую.

Интересный факт про центрированный обход (**LNR**), если мы возмем какой-то узел из списка **inorder**, то все элменты слева от него будут и в дереве находится где-то слева, а все элементы справа от него будут и в дереве где-то справа. (Ну он же не просто так центрированный)

Теперь мы поняли как рекурсивно разделить задачу.

Возьмем первый элемент из **preorder** с помощью **pop**(). Создадим узел **root** со значением этого элемента. Также нам понадобится вычислить его индекс в массиве **inorder**. Теперь рекурсивно делим задачу на две подзадачи. Для левого поддерева вызываем рекурсивно нашу функцию передавая туда тот же **preorder** (по ссылке, для этого мы делали **pop**(), чтобы не множить расходы памяти) и срез **inorder**[:**indx**] (все узлы которые будут находится в левом поддереве). Аналогично делаем для правого поддереве, только берем срез **inorder**[**indx**+**1**:] (только правые узлы). В конце возвращаем **root**.

Вроде бы всё хорошо, но есть одна проблемка. Это линейный поиск индекса **indx**, который увеличивает асимптотику времени в **N** раз.

Это можно исправить, если заменить массив **inorder** хэш-таблицей, в которой ключом будет значение **i**-того элемента, а его значением индекс **i**.

Тогда нам нужно немного изменить нашу рекурсивную функцию, таким образом, чтобы она работала не со срезами массива **inorder** а с двумя индексами.

Такая оптимизация позволит убрать эту лишнюю временную сложность.



## **Оценка:**

С хэш-таблицей мы получим сложность **O**(**N**) по времени, где **N** - длина **preorder** (количество узлов в дереве). Поиск в хэш таблице выполняется за **O**(**1**), в отличии от массива, где поиск **O**(**N**), поэтому мы избежали **O**(**N**^**2**). По памяти мы тратим **O**(**N**) на хэш таблицу. (+ помним про стек рекурсии)

## Код:
```python
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree1(
        self,
        preorder: list[int],
        inorder: list[int],
    ) -> Optional[TreeNode]:
        return self.build1(preorder, inorder)

    def build(
        self,
        preorder: list[int],
        inorder: list[int],
    ) -> Optional[TreeNode]:
        if inorder:
            indx = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[indx])

            root.left = self.build(preorder, inorder[:indx])
            root.right = self.build(preorder, inorder[indx + 1 :])

            return root

        return None

    def buildTree2(
        self,
        preorder: list[int],
        inorder: list[int],
    ) -> Optional[TreeNode]:
        mapping = {}

        for i in range(len(inorder)):
            mapping[inorder[i]] = i

        def build(start: int, end: int) -> Optional[TreeNode]:
            if start > end:
                return None

            mid = mapping[preorder.pop(0)]
            root = TreeNode(inorder[mid])

            root.left = build(start, mid - 1)
            root.right = build(mid + 1, end)

            return root

        return build(0, len(preorder) - 1)

```

<div align='center'><h3><a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/71.Symmetric%20Tree'>⬅️ предыдущая задача</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/README.md'>Все задачи</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/73.Construct%20Binary%20Tree%20from%20Inorder%20and%20Postorder%20Traversal'>следующая задача ➡️</a></h3></div>