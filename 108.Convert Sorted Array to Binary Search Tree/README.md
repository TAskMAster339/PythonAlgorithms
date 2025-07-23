<div align='center'>
<h1><a href='https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/'><strong>108) Convert Sorted Array to Binary Search Tree</strong></a></h1>
</div>

## **Условие:**

Дан массив целых чисел **nums**, где элементы отсортированы в возрастающем порядке, сконвертируйте его в бинарное дерево поиска **BST**, в котором глубина любых двух поддеревьев узла отличается не больше, чем на **1**

## **Идея:**

Смотри гифку

## **Реализация:**

Из гифки мы заметим, что если мы возьмем за корень середину массива, то все элементы слева от неё будут находится в левом поддереве, а все элементы справа от середины будут находится в правом поддереве. Подзадачи решаются аналогичным способом.

Создадим рекурсивную функцию, которая будет как бы делать **DFS** по массиву. Такой обход по массиву позволит нам построить **BST** с одинаковыми глубинами.

Крайний случай, когда **left** > **right**, то возвращаем **None**, так как такого числа нет в массиве.

Рекуррентный случай, мы высчитываем середину, создаем узел и рекуррентно вызываем нашу функцию для лево и правого поддерева.



## **Оценка:**

Верхняя граница по времени будет **O**(**N**), где **N** - длина массива **N**, потому что нам необходимо пройти по всем элементам массива.

Верхняя граница по памяти будет **O**(**logN**), это расходы на стек вызова функций. Максимальная глубина рекурсии, которая у нас может быть **logN**, поэтому в наихудшем случае у нас будет **O**(**logN**) элементов в стеке.

## Код:
```python
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> Optional[TreeNode]:
        def convert(left, right) -> TreeNode:
            if left > right:
                return None
            mid = (left + right) // 2

            root = TreeNode(nums[mid])

            root.left = convert(left, mid - 1)
            root.right = convert(mid + 1, right)

            return root

        return convert(0, len(nums) - 1)

```

<div align='center'><h3><a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/107.Word%20Search'>⬅️ предыдущая задача</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/README.md'>Все задачи</a></h3></div>