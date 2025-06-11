<div align='center'>
<h1><a href='https://leetcode.com/problems/evaluate-division/description/'><strong>92) Evaluate Division</strong></a></h1>
</div>

## **Условие:**

Дан массив пар переменных **equations** и массив вещественных чисел **values**, где **equations**[**i**] = [**A_i**, **B_i**] и **values**[**i**] представляют собой следующие выражение - **A_i** / **B_i** = **values**[**i**]. Каждая переменная **A_i**, **B_i** представляет одну переменную.

Также дан массив выражений **queries**, в котором **queries**[**j**] = [**C_j**, **D_j**], нужно вернуть массив вычисленных значений **C_j** / **D_j**. Если однозначного ответа нет, то необходимо ответ будет -**1**.

Все входные данные корректны. Если переменные из **queries** не появлялись в **equations**, то их значение **undefined**

## **Идея:**

Представить переменные из **equations** в качестве вершин графа, а значения **values** будут весами соответствующих ребер между вершинами

## **Реализация:**

Сначала необходимо реализовать удобную нам структура данных, которая будет представлять граф. Это будет словарь, где ключом будет переменная из **equations**, а значением список ребер. Ребром будет кортеж, состоящий из узла и его веса — {**a**: [(**b**, **5**)]} (**a** -**5**-> **b**).

Теперь нужно пройтись по всем парам из **queries**. Если хотя бы одного элемента пары нет в словаре, то значение этого выражения -**1**. Если оба значения есть в словаре, но они одинаковые, то выражение равно **1**. Во всех остальных случаях необходимо вычислить длину пути от первой вершины до второй.

Путь в данной задаче будет УМНОЖАТЬСЯ, а не складываться, так как веса представляют собой отношения переменных, в данном графе путь представляет собой произведение отношений.

Например, граф: | **a** -**2**-> **b** -**3**-> **c** |, тогда отношение **a** / **c** = (**a** / **b**) * (**b** / **c**) = **2** * **3** = **6**.

Для расчета пути я реализовал **DFS**, который динамически высчитывает путь. Можно воспользоваться **BFS**. (Из-за условий задачи можно воспользоваться алгоритмом Дейкстры)



Примечание:

Если бы у нас стояла задачи найти все возможные значения **queries**, либо длина **queries** была бы очень велика, то эффективнее было бы воспользоваться алгоритмом Флойда-Уоршелла. Но так как у нас длина **queries** <= **20** (Также есть **undefined** выражения), то наше решение эффективно, хотя при масштабировании оно станет плохим.



## **Оценка:**

Создание графа займет **O**(**N**), где **N** - количество исходных выражений **equations**. Расчет всех выражений **queries** займет **O**(**M** * **N**), **M** - длина **queries**. (В наихудшем случае каждый раз будем вызывать **DFS**, который в наихудшем случае пройдет по всем узлам, которых в наихудшем случае будет **N** (на самом деле **сN** + **t**, но **c**, **t** - какие-то константы, которыми можно пренебречь по сравнению с **N**)). Итого верхняя граница по времени будет **O**(**NM**).

Верхняя граница по памяти будет **O**(**N**). Графу нужно **O**(**N**), стек рекурсии тоже хочет **O**(**N**), множество для уже посещенных вершин тоже **O**(**N**).

## Код:
```python
class Solution:
    def calcEquation(
        self,
        equations: list[list[str]],
        values: list[float],
        queries: list[list[str]],
    ) -> list[float]:

        graph = {}
        for i in range(len(equations)):
            node_start = equations[i][0]
            node_end = equations[i][1]
            if node_start not in graph:
                graph[node_start] = []
            if node_end not in graph:
                graph[node_end] = []
            graph[node_start].append((node_end, values[i]))
            graph[node_end].append((node_start, 1 / values[i]))


        def dfs(start: str, target: str, visited: set, path: float) -> float:
            if start == target:
                return path

            visited.add(start)
            for node, path_len in graph[start]:
                if node not in visited:
                    result = dfs(node, target, visited, path*path_len)
                    if result != -1:
                        return result
            return -1

        result = []
        for start, target in queries:
            if start not in graph or target not in graph:
                result.append(-1.0)
            elif start == target:
                result.append(1.0)
            else:
                visited = set()
                result.append(dfs(start, target, visited, 1))

        return result

if __name__ == "__main__":
    s = Solution()
    print(s.calcEquation(
        [["a","b"],["b","c"]],
        [2.0,3.0],
        [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]],
    ))

```

<div align='center'><h3><a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/91.Clone%20Graph'>⬅️ предыдущая задача</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/README.md'>Все задачи</a></h3></div>