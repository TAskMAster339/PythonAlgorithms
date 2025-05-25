<div align='center'>
<h1><a href='https://leetcode.com/problems/valid-anagram/description/'><strong>42) Valid Anagram</strong></a></h1>
</div>

## **Условие:**

Даны две строки **s** и **t**, нужно вернуть **True**, если строка **t** является анаграммой строки **s**, иначе **False**.

Анаграмма - слово, которое получено перестановкой букв в другом слове.

## **Идея:**

Нужно проверить, что были использованы все буквы.

## **Реализация:**

Сначала проверим длины строк. Для того, чтобы слова были анаграммами они должны быть одинаковы.

Создадим словарь **table**. Заполним его частотами букв строки **s**.

Затем пройдем по буквам строки **t**. Если буквы нет в словаре, возвращаем **False**, в строке **t** есть какая-то буква, которой нет в **s**. Если буква есть в словаре, уменьшим её значение на **1**. Затем если значение стало отрицательным, то это значит, что у нас нехватка букв для анаграммы, возвращаем **False**.

Если не случился ни один **return**, то строка **t** является анаграммой **s**, возвращаем **True**.



После цикла чему будут равны частоты в словаре? Подумайте почему так получается.



## **Оценка:**

По времени мы затратим **O**(**N**), где **N** длина строки **s**. По памяти мы потратим **O**(**1**).

## Код:
```python
from util import test_case


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        table = dict()

        if len(t) != len(s):
            return False

        for char in s:
            if char in table:
                table[char] += 1
            else:
                table[char] = 1

        for char in t:
            if char not in table:
                return False
            table[char] -= 1
            if table[char] < 0:
                return False

        return True


if __name__ == "__main__":
    s = Solution().isAnagram
    test_case(s, True, s="anagram", t="nagaram")
    test_case(s, False, s="rat", t="car")

```

<div align='center'><h3><a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/41.Word%20Pattern'>⬅️ предыдущая задача</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/README.md'>Все задачи</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/43.Group%20Anagrams'>следующая задача ➡️</a></h3></div>