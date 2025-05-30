<div align='center'>
<h1><a href='https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/'><strong>23) Find the Index of the First Occurrence in a String</strong></a></h1>
</div>

## **Условие:**

Даны две строки **needle** и **haystack**, нужно вернуть индекс первого появления строки **needle** в **haystack**, или -**1**, если **needle** нет в **haystack**.

## **Идея:**

Как лучше всего искать иголку в стоге сена?

## **Реализация:**

Решение в одну строку: **heystack**.**find**(**needle**). Прекрасный встроенный метод в **Python**, который находит индекс вхождение **needle** в **haystack**, причем делает это слева на право, и возвращает -**1**, если не найдено.

Для справки, такой поиск реализуется одним циклом. Где мы походим по буквам **haystack**, если мы находим первую букву **needle**, мы записываем её индекс, затем проверяем, что все следующие буквы будут равны буквам **needle**, если это так возвращаем этот индекс, иначе присваеваем ему -**1** и идем дальше, надеясь, что найти строку **needle** в другом месте.

## **Оценка:**

По времени мы потратим **O**(**N**), по памяти **O**(**1**), так как мы не создали ни одной переменной.

## Код:
```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


if __name__ == "__main__":
    s = Solution()
    print(s.strStr("sadbutsad", "sad"))
    print(s.strStr("leetcode", "leeto"))

```

<div align='center'><h3><a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/22.Zigzag%20Conversion'>⬅️ предыдущая задача</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/README.md'>Все задачи</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/24.Text%20Justification'>следующая задача ➡️</a></h3></div>