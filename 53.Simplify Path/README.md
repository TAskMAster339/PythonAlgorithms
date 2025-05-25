<div align='center'>
<h1><a href='https://leetcode.com/problems/simplify-path/description/'><strong>53) Simplify Path</strong></a></h1>
</div>

## **Условие:**

Вам дан абсолютный путь файловой системы **UNIX** типа. Нужно представить этот абсолютный путь в виде упрощенного канонического пути.

У **UNIX** типа файловой системы есть следующие правила:

**1**) /. представляет собой текущую директорию

**2**) /.. представляет собой предыдущую директорию

**3**) // или /// и т.д. эквивалентно одному слешу /

**4**) Любая последовательность ".", которая не соответствует вышеуказанным правилам, следует интерпретировать как валидное имя директории. (Например, .... или .....)

Упрощенный канонический путь соответствует следующим правилам:

**1**) Путь должен начинаться с одиночного слеша /

**2**) Директории в пути должны быть разделены ровно одним слешом /

**3**) Путь не может оканчиваться на слеш /, за исключением корневой директории. ("/ ")

**4**) Путь не содержит "." и "..".

## **Идея:**

Хорошо понять, что путь представляет собой стек директорий, по которым мы прошли.

## **Реализация:**

Разделим путь по слешам "/" с помощью .**split**("/"). Затем проитерируемся по элементам массива, если элемент точка, то делаем **continue** по циклу, если две точки, то убираем верхний элемент из стека. Во всех остальных случаях добавляем элемент в стек.

В конце нужно вернуть элементы стека, соединенные "/". Это и будет упрощенный канонический путь.



## **Оценка:**

По времени оценка следующая: **O**(**N**), где **N** - длина входной строки **path**. По памяти **O**(**1**).

## Код:
```python
from util import test_case


class Solution:
    def simplifyPath(self, path: str) -> str:
        path_words = path.split("/")
        stack = []
        for word in path_words:
            if not word:
                continue
            else:
                if word == ".":
                    continue
                elif word == "..":
                    if stack:
                        stack.pop()
                else:
                    stack.append(word)
        return "/" + "/".join(stack)


if __name__ == "__main__":
    f = Solution().simplifyPath
    test_case(f, "/home", path="/home/")
    test_case(f, "/home/foo", path="/home//foo/")
    test_case(f, "/home/user/Pictures", "/home/user/Documents/../Pictures")
    test_case(f, "/", "/../")
    test_case(f, "/.../b/d", "/.../a/../b/c/../d/./")

```

<div align='center'><h3><a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/52.Valid%20Parentheses'>⬅️ предыдущая задача</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/README.md'>Все задачи</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/54.Min%20Stack'>следующая задача ➡️</a></h3></div>