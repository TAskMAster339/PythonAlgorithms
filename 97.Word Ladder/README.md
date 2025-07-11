<div align='center'>
<h1><a href='https://leetcode.com/problems/word-ladder/description/'><strong>97) Word Ladder</strong></a></h1>
</div>

## **Условие:**

Трансформационная последовательность, начинающаяся с **beginWord** и заканчивающаяся **endWord**, составленная с помощью словаря **wordList** это последовательность **beignWord** -> **s1** -> **s2** -> ... -> **endWord**.

Каждая пара в этой последовательности отличается только одним символом. Каждый из **s1**, **s2**, ... , **si** находится в **wordList**.

Необходимо посчитать длину такой трансформационной последовательности

## **Идея:**

Точно такое же решение как и у предыдущей задачи, только нужно немного оптимизировать, чтобы пройти по времени

## **Реализация:**

Первая оптимизация - создать множество из **wordList**, так как операции с множеством будут намного быстрее, чем с массивом.

Вторая оптимизация мы будем идти не по всем словам в **wordList**, а будем создавать близкие слова. Всего близких слов (которые отличаются одним символом) будет **M** * **K**, где **M** - длина слова, а **K** - мощность алфавита. Если наше созданное слово есть в множестве, то мы добавляем это слово в очередь и удаляем его из множества. (Таким образом множество будет хранить только те элементы, которые мы еще не обошли, оно будет аналогом множества **visited** из предыдущего решения)



## **Оценка:**

Таким образом мы получим итоговую сложность **O**(**NMK**), где **N** - размер **wordList**. **K** = **26** - количество символов в английском алфавите. В предыдущем алгоритме сложность была **O**(**NNK**). Коэффициентом **K** можно пренебречь, но для строгости пускай будет. Мы оптимизировали от квадратичной сложности, до линейной, так как **M** в среднем будет много меньше, чем **N** (по условиям задачи **1** <= **M** <= **10**).

По памяти оценка останется точно такой же: **O**(**N**)

## Код:
```python
from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        wordSet = set(wordList)

        if endWord not in wordSet:
            return 0

        queue = deque([(beginWord, 1)])

        while queue:
            word, path_len = queue.popleft()
            if word == endWord:
                return path_len
            for i in range(len(word)):
                for char in "abcdefghijklmnopqrstuvwxyz":
                    new_word = word[:i] + char + word[i + 1 :]
                    if new_word in wordSet:
                        wordSet.remove(new_word)
                        queue.append((new_word, path_len + 1))

        return 0


if __name__ == "__main__":
    f = Solution().ladderLength
    print(f("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
    print(f("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))

```

<div align='center'><h3><a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/96.Minimum%20Genetic%20Mutation'>⬅️ предыдущая задача</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/README.md'>Все задачи</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/98.Implement%20Trie%20(Prefix%20Tree)'>следующая задача ➡️</a></h3></div>