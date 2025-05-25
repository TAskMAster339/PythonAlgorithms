# [**41) Word Pattern**](https://leetcode.com/problems/word-pattern/description/)

## **Условие:**

Дана шаблонная строка **pattern** и строка **s**, нужно выяснить соответствует ли строка **s** шаблону **pattern**.

Под соответствием шаблону понимается:

Каждая буква в **pattern** соответствует ровно одному уникальному слову в **s**. Каждый уникальное слово в **s** соответствует ровно одной букве в **pattern**. Не существует двух букв, соответствующих одному и тому же слову, и наоборот.

## **Идея:**

Смотри предыдущую задачу

## **Реализация:**

Делаем то же самое, только теперь у нас в качестве одной строки выступает массив строк. Просто представляем, что эти строки - буквы и делаем то же самое, что делали в предыдущей задаче.



## **Оценка:**

По времени мы затратим **O**(**N**), где **N** - длина строки **s** (Из-за метода .**split**()). Цикл в котором мы будем проверять шаблон пройдет за **O**(**K**), где **K** - длина строки **pattern**, но **K** много меньше **N**, поэтому итоговая верхняя граница будет равна **O**(**N**), по памяти мы потратим **O**(**1**).

## Код:
```python
from util import test_case


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        table = dict()

        arr = s.split()
        if len(pattern) != len(arr):
            return False

        for i in range(len(arr)):
            word = arr[i]
            char = pattern[i]
            if char in table:
                if table[char] != word:
                    return False
            else:
                if word in table.values():
                    return False
                table[char] = word
        return True


if __name__ == "__main__":
    s = Solution().wordPattern
    test_case(s, True, "abba", "dog cat cat dog")
    test_case(s, False, "abba", "dog cat cat fish")
    test_case(s, False, "aaaa", "dog cat cat dog")
    test_case(s, False, "abba", "dog dog dog dog")

```

### [<-- предыдущая задача](https://github.com/TAskMAster339/PythonAlgorithms/tree/main/40.Isomorphic%20Strings) | [следующая задача -->](https://github.com/TAskMAster339/PythonAlgorithms/tree/main/42.Valid%20Anagram)
