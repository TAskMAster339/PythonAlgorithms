<div align='center'>
<h1><a href='https://leetcode.com/problems/isomorphic-strings/description/'><strong>40) Isomorphic Strings</strong></a></h1>
</div>

## **Условие:**

Дано две строки **s** и **t**, нужно понять являются ли они изоморфными.

Две строки изоморфны, если каждой букве первой строки соответствует ровно одна буква второй строки, притом одинаковым буквам должна соответствовать одна и та же буква, и наоборот

Например, строка **paper** изоморфна **title**. Для первого слова **p**->**t**, **a**->**i**, **e**->**l**, **r**->**e**. Для второго слова **t**->**p**, **i**->**a**, **l**->**e**, **e**->**r**.

## **Идея:**

Нужно просто проверять наличие только одного соответствия между буквам с одной и с другой стороны.

## **Реализация:**

Создадим словарь **table**. Теперь с помощью цикла будем заполнять его соответствиями, то есть ключ - символ строки **s**, значение - символ строки **t**.

Если символа строки **s** еще нет в таблице, то мы проверяем есть ли символ строки **t** в значениях таблице, если он там будет, то это значит, что у нас есть как минимум два символа в строке **s**, соответствующих одному и тому же символу строки **t**, что нарушает изоморфность, поэтому возвращаем **False**. Иначе добавляем символ строки **t** по символу строки **s** в таблицу.

Если символ строки **s** есть в таблице, то мы проверяем, что значение, которое лежит по этому ключу, соответствует ново-полученному символу строки **t**, если это не так возвращаем **False**.

Если после окончания цикла, мы не вышли из функции, значит строки изоморфны, возвращаем **True**.



## **Оценка:**

Оценка по времени **O**(**N**), **a** по памяти **O**(**1**).

## Код:
```python
from util import test_case


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        table = dict()
        for c in range(len(s)):
            char1 = s[c]
            char2 = t[c]
            if char1 not in table:
                if char2 in table.values():
                    return False
                table[char1] = char2
            else:
                if table[char1] != char2:
                    return False
        return True


if __name__ == "__main__":
    s = Solution().isIsomorphic
    test_case(s, True, "egg", "add")
    test_case(s, False, "foo", "bar")
    test_case(s, True, "paper", "title")
    test_case(s, False, "badc", "baba")
    test_case(s, False, "egcd", "adfd")

```

<div align='center'><h3><a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/39.Ransom%20Note'>⬅️ предыдущая задача</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/README.md'>Все задачи</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/41.Word%20Pattern'>следующая задача ➡️</a></h3></div>