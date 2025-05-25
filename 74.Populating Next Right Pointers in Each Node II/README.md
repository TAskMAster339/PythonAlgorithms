<div align='center'>
<h1><a href='https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/description/'><strong>74) Populating Next Right Pointers in Each Node II</strong></a></h1>
</div>

## **Условие:**

Дано бинарное дерево. У каждого узла есть поле **next**. Нужно заполнить каждое поле **next** так, чтобы оно указывало на узел справа от него. Если такого нет, то нужно вернуть **None**. По умолчанию, все указатели **next** равны **None**

## **Идея:**

**DFS** тут не сработает, поэтому берем **BFS**

## **Реализация:**

Создадим очередь, в которой будем хранить пары значений: (**node**, **level**). **Level** нужен для того, чтобы можно было понять находяться ли узлы на одном и том же уровне. Также понадобится пара **prev_node**. В которой будет храниться предыдущий узел и его уровень.

Теперь немного изменив алгоритм поиска в ширину, пройдемся по дереву. (Мы будем идти справа налево, потому что спускаясь справа вот так вот выйдет, что указатель **next** у самого правого узла не измениться и останется **None**). Если узел не **None**, то мы обновляем его **next**, если **prev_node** находится с ним на одном уровне, затем обновляем **prev_node**. В конце не забываем добавить в очередь правое поддерево с **level** + **1** и левое поддерево тоже с **level** + **1**.



Также я нашел одно гениальное решение. Идея простая, но как до такого додуматься хз. Если посмотреть на наши уровни дерева, то можно заметить, что они очень похожи на связный список, только его забыли связать друг с другом. Поэтому мы можем пройтись по детям узлов, связывая их друг с другом. Таким образом мы не только красиво решим задачу, но и еще сэкономим память.



## **Оценка:**

Мое решение по времени **O**(**N**), где **N** - количество узлов в дереве, но по памяти **O**(**N**), так как используется очередь, а в наихудшем случае она будет заполнена полностью. В гениальном решении очереди нет, поэтому затраты по памяти будут **O**(**1**).

## Код:
```python
class Node:
    def __init__(
        self,
        val: int = 0,
        left: "Node" = None,
        right: "Node" = None,
        next: "Node" = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: "Node") -> "Node":
        queue = [(root, 0)]
        prev_node = (None, 0)

        while queue:
            node, level = queue.pop(0)
            if node:
                if prev_node[1] == level:
                    node.next = prev_node[0]
                prev_node = (node, level)
                queue.append((node.right, level + 1))
                queue.append((node.left, level + 1))

    def connect2(self, root: "Node") -> "Node":
        if not root:
            return None

        curr = root
        dummy = Node(-999)
        head = root

        while head:
            curr = head  # initialize current level's head
            prev = dummy  # init prev for next level linked list traversal
            # iterate through the linked-list of the current level and
            # connect all the siblings in the next level
            while curr:
                if curr.left:
                    prev.next = curr.left
                    prev = prev.next
                if curr.right:
                    prev.next = curr.right
                    prev = prev.next
                curr = curr.next
            head = dummy.next  # update head to the linked list of next level
            dummy.next = None  # reset dummy node
        return root

```

<div align='center'><h3><a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/73.Construct%20Binary%20Tree%20from%20Inorder%20and%20Postorder%20Traversal'>⬅️ предыдущая задача</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/README.md'>Все задачи</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/75.Flatten%20Binary%20Tree%20to%20Linked%20List'>следующая задача ➡️</a></h3></div>