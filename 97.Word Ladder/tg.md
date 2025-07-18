**97) Word Ladder**
https://leetcode.com/problems/word-ladder/description/
**Условие:**
Трансформационная последовательность, начинающаяся с **beginWord** и заканчивающаяся **endWord**, составленная с помощью словаря **wordList** это последовательность **beignWord** -> **s1** -> **s2** -> ... -> **endWord**.
Каждая пара в этой последовательности отличается только одним символом. Каждый из **s1**, **s2**, ... , **si** находится в **wordList**.
Необходимо посчитать длину такой трансформационной последовательности
**Идея:**
Точно такое же решение как и у предыдущей задачи, только нужно немного оптимизировать, чтобы пройти по времени
**Реализация:**
    Первая оптимизация - создать множество из **wordList**, так как операции с множеством будут намного быстрее, чем с массивом.
    Вторая оптимизация мы будем идти не по всем словам в **wordList**, а будем создавать близкие слова. Всего близких слов (которые отличаются одним символом) будет **M** * **K**, где **M** - длина слова, а **K** - мощность алфавита. Если наше созданное слово есть в множестве, то мы добавляем это слово в очередь и удаляем его из множества. (Таким образом множество будет хранить только те элементы, которые мы еще не обошли, оно будет аналогом множества **visited** из предыдущего решения) 

**Оценка:**
    Таким образом мы получим итоговую сложность **O**(**NMK**), где **N** - размер **wordList**. **K** = **26** - количество символов в английском алфавите. В предыдущем алгоритме сложность была **O**(**NNK**). Коэффициентом **K** можно пренебречь, но для строгости пускай будет. Мы оптимизировали от квадратичной сложности, до линейной, так как **M** в среднем будет много меньше, чем **N** (по условиям задачи **1** <= **M** <= **10**).
    По памяти оценка останется точно такой же: **O**(**N**)
