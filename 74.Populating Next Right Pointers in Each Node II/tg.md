**74) Populating Next Right Pointers in Each Node II**
https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/description/
**Условие:**
Дано бинарное дерево. У каждого узла есть поле **next**. Нужно заполнить каждое поле **next** так, чтобы оно указывало на узел справа от него. Если такого нет, то нужно вернуть **None**. По умолчанию, все указатели **next** равны **None**
**Идея:**
**DFS** тут не сработает, поэтому берем **BFS**
**Реализация:**
    Создадим очередь, в которой будем хранить пары значений: (**node**, **level**). **Level** нужен для того, чтобы можно было понять находяться ли узлы на одном и том же уровне. Также понадобится пара **prev_node**. В которой будет храниться предыдущий узел и его уровень.
    Теперь немного изменив алгоритм поиска в ширину, пройдемся по дереву. (Мы будем идти справа налево, потому что спускаясь справа вот так вот выйдет, что указатель **next** у самого правого узла не измениться и останется **None**). Если узел не **None**, то мы обновляем его **next**, если **prev_node** находится с ним на одном уровне, затем обновляем **prev_node**. В конце не забываем добавить в очередь правое поддерево с **level** + **1** и левое поддерево тоже с **level** + **1**.

    Также я нашел одно гениальное решение. Идея простая, но как до такого додуматься хз. Если посмотреть на наши уровни дерева, то можно заметить, что они очень похожи на связный список, только его забыли связать друг с другом. Поэтому мы можем пройтись по детям узлов, связывая их друг с другом. Таким образом мы не только красиво решим задачу, но и еще сэкономим память.

**Оценка:**
    Мое решение по времени **O**(**N**), где **N** - количество узлов в дереве, но по памяти **O**(**N**), так как используется очередь, а в наихудшем случае она будет заполнена полностью. В гениальном решении очереди нет, поэтому затраты по памяти будут **O**(**1**).
