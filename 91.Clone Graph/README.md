<div align='center'>
<h1><a href='https://leetcode.com/problems/clone-graph/description/'><strong>91) Clone Graph</strong></a></h1>
</div>

## **Условие:**

Дана ссылка на узел в связном неориентированном графе. Нужно вернуть глубокую копию (клона) графа. Каждый узел графа содержит целочисленное значение **val** и список соседних узлов **neighbors**

## **Идея:**

**Tупо** пройтись по графу и копировать узлы. Только есть одна проблема, нужно как-то запоминать уже скопированные узлы, чтобы не создать лишние копии

## **Реализация:**

Для хранения уже скопированных узлов будем использовать хэш-таблицу. В качестве ключа мы выберем **val**, в качестве значения будет копия соответствующего узла. (Мы можем это сделать, потому что условие гарантирует уникальность **val**)

Далее с помощью **BFS** пройдемся по графу. Наша задача будет брать какой-то узел и копировать его соседей. Если соседа еще нет в хэш-таблице, то запишем его туда и добавим этого соседа в очередь. Если сосед есть в хэш-таблице, значит мы уже скопировали этот узел, делать это повторно нет смысла, поэтому достаем из таблицы ссылку и записываем её в **neighbors**. В конце присваиваем скопированному узлу массив скопированных соседей.

В конце возвращаем копию узла, ссылку на которого нам дали в начале.



## **Оценка:**

По времени верхняя граница будет **O**(**V** + **E**), где **V** - количество вершин в графе, **E** - количество ребер в графе. За одну итерацию мы будем обрабатывать одну вершину и все её ребра. Сложность одной итерации - число **1** + **e**. (**1** - вершина, **e** - количество её ребер). Тогда сложность всех итераций будет суммой всех этих чисел. (Это утверждение рекомендую попробовать доказать) Сумма всех вершин даст **V**, сумма всех ребер даст **E**. Отсюда итоговая сложность **O**(**V** + **E**). По памяти верхняя граница будет **O**(**V**), расходы на хэш-таблицу и очередь.

## Код:
```python
from typing import Optional

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return None
        table = {node.val: Node(node.val)}
        queue = [node]
        while queue:
            curr_node = queue.pop(0)
            curr_node_copy = table[curr_node.val]
            neighbors = []
            for n in curr_node.neighbors:
                if n.val not in table:
                    table[n.val] = Node(n.val)
                    queue.append(n)
                neighbors.append(table[n.val])
            curr_node_copy.neighbors = neighbors

        return table[node.val]

```

<div align='center'><h3><a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/90.Surrounded%20Regions'>⬅️ предыдущая задача</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/README.md'>Все задачи</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/92.Evaluate%20Division'>следующая задача ➡️</a></h3></div>