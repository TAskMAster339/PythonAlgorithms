<div align='center'>
<h1><a href='https://leetcode.com/problems/implement-trie-prefix-tree/description/'><strong>98) Implement Trie (Prefix Tree)</strong></a></h1>
</div>

## **Условие:**

**Trie** - префиксное дерево - структура данных, которая используется для эффективного хранения и использования множество строковых ключей. Чаще всего используется для автокомплита или проверки правописания

Необходимо реализовать класс **Trie**.

Метод **void** **insert**(**String** **word**) добавляет строку в дерево.

Метод **boolean** **search**(**String** **word**) возвращает **True**, если **word** находиться в дерево, иначе **False**.

Метод **boolean** **startsWith**(**String** **prefix**) возвращает **True**, если в дереве присутствует слово **word** с префиксом **prefix**, иначе **False**

## **Идея:**

**Trie** - это дерево, где в узлах лежат буковки, нужно просто как-то это оптимизировать

## **Реализация:**

Создадим вспомогательный класс для узла **TrieNode**, у него будут поля **children** (словарь для хранения пар символ-узел) и **is_end** (флаг, который потребуется для понимания, где окончилось слово).

При создании дерева создадим корневой узел **root**.

При вставке элемента мы будем идти циклом по символам слова и записывать в **node**.**children**[**char**] = **TrieNode**(). Тупо будем строить дерево из символов. В конце важно не забыть обновить флаг **node**.**is_end** = **True**. Это понадобиться нам для поиска.

При поиске элемента делаем то же самое: спускаемся по дереву, пытаемся спуститься на высоту **len**(**word**). Если не получилось (дерева там нету), то возвращаем **False**. Если получилось возвращаем **node**.**is_end**. (Если нам повезло и мы спустились и получили какое-то слово в дереве, то нужно с помощью флага проверить было ли оно целенаправленно вставлено ранее (Например, вставляем слово "**abcd**", ищем слово "**abc**", оно окажется в дереве, но по счастливой случайности, поэтому **search**("**abc**") -> **False**)).

При поиске префикса мы делаем тот же самый алгоритм, как и при поиске, но в конце мы должны вернуть **True**, вместо **node**.**is_end**, потому что мы ищем **prefix**, а не полноценное слово.



## **Оценка:**

Верхняя оценка по времени будет **O**(**N**), где **N** - глубина (высота) дерева, или же длина слова. По памяти оценка уже поинтересней. Пусть мы будем хранить **M** слов, тогда для каждого символа слова, находящегося в той или иной позиции, будет какое-то место в дереве. Всего в наихудшем случае будет **O**(**MN**) узлов в дереве. Оценку можно упростить до **O**(**M**), так как **N** << **M** (**N** - длина слова (Например, в английском языке средняя длина слова **4**.**7**, в а русском **5**.**28**))

## Код:
```python
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

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

```

<div align='center'><h3><a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/97.Word%20Ladder'>⬅️ предыдущая задача</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/README.md'>Все задачи</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/99.Design%20Add%20and%20Search%20Words%20Data%20Structure'>следующая задача ➡️</a></h3></div>