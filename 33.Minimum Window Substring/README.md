# [**33) Minimum Window Substring**](https://leetcode.com/problems/minimum-window-substring/description/)

## **Условие:**

Даны две строки **s** и **t** длины **m** и **n** соответственно, нужно вернуть минимальное окно с подстрокой строки **s**, такое что каждый символ в **t** (включая дубликаты) находится в окне. Если такой подстроки нет, нужно вернуть пустую строку. Гарантируется, что решение единственное.

## **Идея:**

Так как в строке **t** могут быть дубликаты, то мы опять реализуем окно через хэш-таблицу.

## **Реализация:**

Если длина строка **s** меньше строки **t**, то возвращаем пустую строку. Далее создадим хэш-таблицу **char_table** (Я воспользовался классом **defaultdict** из **collections**, который при обращении по какому-либо ключу, который отсутствует в таблице, присваивает ему значение по умолчанию ). Заполняем её частотами букв строки **t**.

Теперь создадим переменную **remaining_chars** = **len**(**t**), которая будет нужна для окна, **min_window** = **float**("**inf**"), длина минимального окна, **start** = **0**, указатель на начало окна.

После этого в цикле с помощью переменной итерации **end** (указатель на конец окна) получим символ **s**[**end**]. Если **char_talbe**[**char**] > **0**, значит это нужный нам символ, декрементируем **remaining_chars** и **char_table**[**char**].

Вот тут хочу пояснить, что означают числа в нашей таблице: если число больше **0**, то это значит дефицит данной буквы в окне, равно **0** - у нас ровно одна нужная буква, меньше **0** - у нас есть еще такие буквы в запасе в окне.

Осталось теперь зафиксировать результат, когда **remaining_chars** == **0** минимизируем полученное окно, для этого есть внутренний цикл, который только двигает левый указатель настолько, насколько это возможно. Затем вычисляем минимум и соответствующую ему минимальную строку, после этого двигаем окно на единицу. В конце возвращаем минимальную строку.



## **Оценка:**

Сложность по времени будет **O**(**N** + **M**), так как у нас есть два последовательных цикла в **N** и **M** итераций. (Внутренний цикл имеет асимптотику **O**(**1**)). По памяти мы потратим **O**(**1**), так как нам нужны будут только маленькие английские буквы. (В наихудшем случае в хэш-таблице будет **26** ключей и значений)

## Код:
```python
from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        char_table = defaultdict(int)

        for char in t:
            char_table[char] += 1

        remaining_chars = len(t)
        min_window = float("inf")
        result = ""
        start = 0

        for end in range(len(s)):
            char = s[end]
            if char_table[char] > 0:
                remaining_chars -= 1
            char_table[char] -= 1

            if remaining_chars == 0:
                while True:
                    first_char = s[start]
                    if char_table[first_char] == 0:
                        break
                    char_table[first_char] += 1
                    start += 1

                if end - start < min_window:
                    min_window = end - start
                    result = s[start : end + 1]

                char_table[s[start]] += 1
                remaining_chars += 1
                start += 1

        return result


if __name__ == "__main__":
    s = Solution()
    print(s.minWindow("ADOBECODEBANC", "ABC"))
    print(s.minWindow("a", "a"))
    print(s.minWindow("a", "aa"))

```

### [<-- предыдущая задача](https://github.com/TAskMAster339/PythonAlgorithms/tree/main/32.Substring%20with%20Concatenation%20of%20All%20Words) | [следующая задача -->](https://github.com/TAskMAster339/PythonAlgorithms/tree/main/34.Valid%20Sudoku)
