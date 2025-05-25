<div align='center'>
<h1><a href='https://leetcode.com/problems/binary-search-tree-iterator/description/'><strong>79) Binary Search Tree Iterator</strong></a></h1>
</div>

## **Условие:**

Необходимо реализовать класс **BSTIterator**, который представляет собой итератор, который позволяет совершить центрированный обход бинарного дерева поиска.

Метод **next**() возвращает значение указателя.

Метод **hasNext**() возвращает **True**, если еще есть узлы в обходе, иначе **False**

## **Идея:**

Если представить бинарное дерево поиска **BST** в виде отсортированного списка по возрастанию, то центрированный обход будет итераций по этому списку

## **Реализация:**

В конструкторе сохраним узел **root** и инициализируем **stack**.

В методе **next**() мы реализуем **LNR** **DFS**. Сначала добавим все левые узла от **root**. Затем извлекаем элемент **nxt** из стека, его значение мы возвращаем. При этом обновляем **root**, присваивая ему значение **nxt**.**right**. Таким образом **next** будет возвращать элементы в порядке возрастания, начиная с самого маленького.

Метод **hasNext**() возвращает **True**, если стек не пустой или корень не равен **None**, иначе **None**.



## **Оценка:**

По времени метод **next**() будет **O**(**1**), это следует из амортизационного анализа. Если у нас дерево состоит из **N** элементов, то максимальное количество раз, которое мы можем вызвать метод **next**(), равно **N**. В этом случае сложность **N** методов будет **O**(**N**). Следовательно, сложность одного метода будет **O**(**N**) / **N** = **O**(**1**). По памяти мы получим верхнюю границу **O**(**logN**), где **logN** - глубина **BST** (У нас в стеке в наихудшем случае будет **logN** узлов).

## Код:
```python
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.stack = []

    def next(self) -> int:
        while self.root:
            self.stack.append(self.root)
            self.root = self.root.left
        nxt = self.stack.pop()
        self.root = nxt.right
        return nxt.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0 or self.root is not None

```

<div align='center'><h3><a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/78.Binary%20Tree%20Maximum%20Path%20Sum'>⬅️ предыдущая задача</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/README.md'>Все задачи</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/80.Count%20Complete%20Tree%20Nodes'>следующая задача ➡️</a></h3></div>