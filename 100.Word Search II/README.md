<div align='center'>
<h1><a href='https://leetcode.com/problems/word-search-ii/description/'><strong>100) Word Search II</strong></a></h1>
</div>

## **Условие:**

Дана доска **board** размером **m** на **n**, заполненная буквами. Также есть список строк **words**, нужно вернуть все слова, которые есть на доске.

Слово присутствует на доске, если оно может быть составлено с помощью последовательности букв в примыкающих клеточках. Клеточки примыкаются, если они расположены по соседству по горизонтали или по вертикали. Одна и та же клеточка не может использоваться больше одного раза в слове. Смотрите фоточку

## **Идея:**

Представить в виде графа и пройтись **DFS**, только нужно оптимизировать, иначе будет очень долго

## **Реализация:**

Реализуем структуру данных **Trie**, которая была реализована в предыдущих задачах. Заполним её словами из списка **words**. И дальше реализуем **DFS**.

**DFS** будет принимать строку, столбец, слово и множество уже посещенных вершин.

Если пара строка, столбец уже проходились, то мы возвращаемся. Иначе добавляем эту пару в множество. Так же тут мы воспользуемся деревом префиксов для оптимизации. Если наше нынешнее слово не является префиксом в дереве, то можно смело возвращаться, так как это значит, что мы его уже не найдем. Если наше нынешнее слово есть в дереве, значит мы нашли его, записываем в **result**, который вернем в конце, а уже найденное слово удаляем из **Trie**.

В самом **DFS** мы будем запускать еще **4** **DFS** для всех возможных направлений (вверх, вниз, влево, вправо).

В конце нам осталось вызвать наш **DFS**, начиная с каждой клетки доски.

Важный момент - это заполнения множества **visited**. Мы должны в нем хранить только те клетки, буквы которых составляют наше слово! То есть мы еще должны учесть логику удаления из множества. Самый простой способ сделать это через постоянное копирование **visited**, но это дорого по памяти. Лучше всего использовать стек.



## **Оценка:**

Верхняя оценка по времени будет **O**(**NM*****4**^**L**), где **N** - количество строк в доске, **M** - количество столбцов в доске, **L** - средняя длина слова в **words**. Она получается следующим образом. Для каждой клетки доски, которых всего **NM**, будет вызван **DFS**, который будет пытаться построить слово длиной **L**, двигаясь в **4** стороны. Поэтому в наихудшем случае **DFS** будет выполнять **4**^**L** операций. У нас в задаче **L** <= **10**. Хотя средняя длина слова будет всегда меньше.

Верхняя оценка по памяти будет равна **O**(**LK**), где **L** - средняя длина слова, а **K** - количество слов в **words**. Столько памяти мы расходуем на хранение **Trie**. Также есть накладные расходы на стек вызова. Но они тоже будут в наихудшем случае **O**(**LK**).

## Код:
```python
from collections import deque


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end

    def is_prefix(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

    def delete(self, word: str) -> None:
        if not self.search(word):
            return

        nodes = []
        node = self.root
        for char in word:
            nodes.append((char, node))
            node = node.children[char]
        node.is_end = False

        for i in range(len(nodes) - 1, -1, -1):
            char, parent_node = nodes[i]
            current_node = parent_node.children[char]
            if not current_node.is_end and not current_node.children:
                del parent_node.children[char]
            else:
                break


class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        m = len(board)
        n = len(board[0])

        trie = Trie()
        for word in words:
            trie.insert(word)
        result = set()
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

        def dfs(r: int, c: int, path: str, visited: deque) -> None:
            if (r, c) in visited:
                return

            current_word = path + board[r][c]
            if not trie.is_prefix(current_word):
                return

            if trie.search(current_word):
                result.add(current_word)
                trie.delete(current_word)

            visited.append((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    dfs(nr, nc, current_word, visited)
            visited.pop()

        for i in range(m):
            for j in range(n):
                dfs(i, j, "", deque())

        return list(result)


if __name__ == "__main__":
    f = Solution().findWords
    print(  # ["eat","oath"]
        f(
            [
                ["o", "a", "a", "n"],
                ["e", "t", "a", "e"],
                ["i", "h", "k", "r"],
                ["i", "f", "l", "v"],
            ],
            ["oath", "pea", "eat", "rain"],
        ),
    )
    print(f([["a", "b"], ["c", "d"]], ["abcb"]))  # []
    print(f([["a", "a"]], ["aaa"]))  # []
    print(  # ["abcdefg","befa","eaabcdgfa","gfedcbaaa"]
        f(
            [
                ["a", "b", "c"],
                ["a", "e", "d"],
                ["a", "f", "g"],
            ],
            ["abcdefg", "gfedcbaaa", "eaabcdgfa", "befa", "dgc", "ade"],
        ),
    )

```

<div align='center'><h3><a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/99.Design%20Add%20and%20Search%20Words%20Data%20Structure'>⬅️ предыдущая задача</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/README.md'>Все задачи</a></h3></div>