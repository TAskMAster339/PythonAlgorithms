<div align='center'>
<h1><a href='https://leetcode.com/problems/course-schedule/description/'><strong>93) Course Schedule</strong></a></h1>
</div>

## **Условие:**

Всего есть **numCourses** курсов, которые нужно пройти. Каждый курс имеет свой номер от **0** до **numCourses** - **1**. Дан массив **prerequisites**, где **prerequisites**[**i**] = [**a_i**, **b_i**], означает, что перед тем как пройти курс **b_i**, необходимо пройти **a_i**.

Верните **True**, если можно пройти все курсы, иначе **False**

## **Идея:**

Можно представить каждый курс как узел графа, а **prerequisites**[**i**] как ребро. Тогда задача сводится к поиску цикла в графе

## **Реализация:**

Запишем все наши узлы в словарь. Ключ будет **a_i**, значением будет массив [**b_i**, ...] (Можно сделать и наоборот, так как мы ищем цикл, важно только взять одно правило и придерживаться его).

Мы будем искать цикл с помощью **DFS**. С помощью множества **visited** будем отслеживать уже посещенные вершины. Если вершины нет в графе, значит, прохождение этого курса не требует какого-либо другого, возвращаем **True**. Если вершина уже встречалась, то возвращаем **False**, значит мы нашли цикл. Это был крайний случай.

Рекуррентный случай - добавляем нашу вершину в **visited**, и рекурсивно вызываем для связанных вершин нашу **DFS**, если она вернула **False**, значит где-то у связного узла есть цикл, возвращаем **False**. Если узел не связан ни одним циклом с связными с ним узлами, то мы можем возвращать **True**, но перед этим удалим узел из графа (Это необходимо, во-первых, для оптимизации, во-вторых, наш **DFS** может найти мнимый цикл, если оставить узел в словаре).

В конце вызываем **DFS** для всех узлов от **0** до **numCourses** - **1**. Возвращаем **all**() от этих вызовов.



## **Оценка:**

Верхняя оценка по времени будет **O**(**V** + **E**), где **V** - количество вершин, **E** - количество ребер. По памяти мы затратим те же **O**(**V** + **E**) для хранения графа в словаре.

## Код:
```python
class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        if len(prerequisites) == 0:
            return True

        graph = {}
        for start, end in prerequisites:
            if start not in graph:
                graph[start] = []
            graph[start].append(end)

        visited = set()

        def dfs(vert: int) -> bool:
            if vert not in graph:
                return True

            if vert in visited:
                return False

            visited.add(vert)

            for child in graph[vert]:
                if not dfs(child):
                    return False

            del graph[vert]
            return True

        return all(dfs(i) for i in range(numCourses))


if __name__ == "__main__":
    f = Solution().canFinish
    print(f(2, [[1, 0]]))  # true
    print(f(2, [[1, 0], [0, 1]]))  # false
    print(f(5, [[1, 4], [2, 4], [3, 1], [3, 2]]))  # true

```

<div align='center'><h3><a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/92.Evaluate%20Division'>⬅️ предыдущая задача</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/README.md'>Все задачи</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/94.Course%20Schedule%20II'>следующая задача ➡️</a></h3></div>