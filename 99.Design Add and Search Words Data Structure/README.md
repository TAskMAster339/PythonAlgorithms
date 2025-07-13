<div align='center'>
<h1><a href='https://leetcode.com/problems/design-add-and-search-words-data-structure/description/'><strong>99) Design Add and Search Words Data Structure</strong></a></h1>
</div>

## **Условие:**

Создайте дизайн структуры данных, которая поддерживает добавления новых слов и поиск, ранее вставленного слова.

Реализуйте класс **WordDictinary**, который имеет конструктор, метод **void** **addWord**(**word**), который добавляет слово в структуру данных, метод **bool** **search**(**word**). Возвращает **True**, если в структуре есть слово, которое подходит под паттерн **word**. Паттерн **word** может содержать точки ".", которая может принимать значения любого символа. Например под паттерн "**d**.**g**" подходит "**dog**", "**dug**", "**dig**" и т.д.

## **Идея:**

Реализовать **Trie** и воспользоваться **DFS**

## **Реализация:**

По аналогии с предыдущей задачей создадим класс **TrieNode**. В конструкторе объекта создадим корень **root** = **TrieNode**()

Метод добавления будет точно такой же, как и в **Trie**.

Метод поиска уже поинтересней. Создадим внутреннюю функцию **DFS**, которая будет рекурсивно искать слово в нашем **Trie**. Аргументами функции будут выступать **node** и **level**. **Node** - узел дерева, **level** - глубина на которую мы спустились.

Крайним случаем выступит ситуация, когда **level** = **len**(**word**), возвращаем **node**.**is_end**.

В рекуррентном случае у нас **2** варианта действия. Если символ (**word**[**level**]) оказался точкой, то нам не повезло и мы должны проверить всех детей нашего узла. Для каждого ребенка вызываем **dfs**(**child**, **level**+**1**). Возвращаем **any**() от этих вызовов. Если нам повезло, то мы проверяем есть ли символ в дочерних узлах, если нет, то возвращаем **False**, иначе вызываем **dfs** для следующего узла.

Не забываем в функции поиска вернуть **dfs**(**self**.**root**, **0**)



## **Оценка:**

По времени вставка будет выполнена за **O**(**N**), где **N** - длина слова. Поиск слова будет выполняться в наихудшем случае за **O**(**K**^**T** * **N**), где **K** - мощность алфавита или максимальное количество детей у узла, **T** - количество точек в строке. Но амортизационная оценка будет **O**(**N**), так как наш поиск ищет какой-либо путь от корня к листу. Это расстояние будет глубиной дерева, в нашем случае она будет равна **N**. По памяти мы затратим **O**(**NM**), где **M** - количество слов, которые надо хранить.

## Код:
```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word: str) -> bool:
        def dfs(node: TrieNode, level: int) -> bool:
            if level == len(word):
                return node.is_end

            char = word[level]
            if char == ".":
                return any(dfs(child, level + 1) for child in node.children.values())

            if char not in node.children:
                return False

            return dfs(node.children[char], level + 1)

        return dfs(self.root, 0)


if __name__ == "__main__":
    wordDictionary = WordDictionary()
    wordDictionary.addWord("bad")
    wordDictionary.addWord("dad")
    wordDictionary.addWord("mad")
    print(wordDictionary.search("pad"))  # return False
    print(wordDictionary.search("bad"))  # return True
    print(wordDictionary.search(".ad"))  # return True
    print(wordDictionary.search("b.."))  # return True

```

<div align='center'><h3><a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/98.Implement%20Trie%20(Prefix%20Tree)'>⬅️ предыдущая задача</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/README.md'>Все задачи</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/100.Word%20Search%20II'>следующая задача ➡️</a></h3></div>