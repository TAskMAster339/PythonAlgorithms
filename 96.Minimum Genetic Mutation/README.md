<div align='center'>
<h1><a href='https://leetcode.com/problems/minimum-genetic-mutation/description/'><strong>96) Minimum Genetic Mutation</strong></a></h1>
</div>

## **Условие:**

Ген может быть представлен в виде строки длины **8**, которая состоит из комбинации символов '**A**', '**C**', '**G**', '**T**'. Предположим, что нам нужно построить цепочку мутации от гена **startGene** до гена **endGene**. Где под мутации понимается изменение ровно одного символа в строке.

Так же дан банк генов **bank**, в котором записаны все разрешенные мутации.

Необходимо вернуть минимальное количество мутаций, которое необходимо совершить, чтобы мутировать от гена **startGene** до гена **endGene**, используя мутации из банка **bank**. Если мутацию провернуть невозможно, необходимо вернуть -**1**

## **Идея:**

Подход очевидный, каждый ген представляем как узел графа, а ребро - мутация. Тогда нужно снова найти наикратчайший путь в графе

## **Реализация:**

Пойдем с помощью **BFS**. Создадим очередь, в которой будем хранить кортеж из гена и длина мутационного пути до этого гена. Например, в начале добавим (**startGene**, **0**). Также для оптимизации создадим множество **visited**.

Реализуем классический **BFS**. Мы будем перебирать все гены из банка. Условием добавления гена в очередь будет отсутствие гена в **visited** и возможность мутировать в него из текущего гена. (Для этого создадим вспомогательную функцию, которая просто проверяет, что в двух строках есть ровно один отличный символ)

Если наш **gene** из очереди оказался равен **endGene**, то мы возвращаем длину его мутационного пути.

Если **BFS** не нашел путь, то мы возвращаем -**1**.



## **Оценка:**

Верхняя граница по времени будет **O**(**N**^**2**), где **N** - размер банка. (**BFS** пройдет по всем узлам графа (генам) это **O**(**N**) и при этом каждый раз будет итерация по всем генам в банке, которых **O**(**N**), поэтому в итоге получим **O**(**N**^**2**)). Асимптотическая оценка по памяти будет **O**(**N**). Так как все **N** элементов банка мы будем хранить, либо в очереди, либо множестве **visited**.

## Код:
```python
from collections import deque


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:
        if endGene not in bank and startGene != endGene:
            return -1

        def is_near(first_gene: str, second_gene: str) -> bool:
            count = 0
            for i in range(len(second_gene)):  # len(fisrt_gene) == len(second_gene)== 8
                if first_gene[i] != second_gene[i]:
                    count += 1
            return count == 1

        queue = deque()
        queue.append((startGene, 0))
        visited = set()

        while queue:
            gene, path_len = queue.popleft()
            if gene == endGene:
                return path_len
            visited.add(gene)
            for next_gene in bank:
                if next_gene not in visited and is_near(next_gene, gene):
                    queue.append((next_gene, path_len + 1))

        return -1


if __name__ == "__main__":
    f = Solution().minMutation
    print(f("AACCGGTT", "AACCGGTA", ["AACCGGTA"]))
    print(f("AACCGGTT", "AAACGGTA", ["AACCGGTA", "AACCGCTA", "AAACGGTA"]))

```

<div align='center'><h3><a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/95.Snakes%20and%20Ladders'>⬅️ предыдущая задача</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/README.md'>Все задачи</a></h3></div>