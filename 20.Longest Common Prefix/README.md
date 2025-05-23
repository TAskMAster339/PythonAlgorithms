# [**20) Longest Common Prefix**](https://leetcode.com/problems/longest-common-prefix/description/)

## **Условие:**

Нужно написать функцию, которая находит наибольший общий префикс среди массива строк, если такого нет, то нужно вернуть пустую строку ""

## **Идея:**

Наибольший общий префикс будет либо равен, либо меньше самой короткой строки.

## **Реализация:**

Создадим переменную **prefix**, в которой будем хранить самый длинный общий префикс. Далее запишем в нее самую короткую строку в массиве. Это будет начальное значение **prefix**. Теперь мы будем пробегаться по всем строкам в массиве, находя наибольший общий префикс среди **i**-того слова и **prefix**. В конце нужно вернуть **prefix**.

## **Оценка:**

По времени мы потратим **O**(**N**), хотя точная оценка будет **O**(**N*****K**), так как вложенный цикл **for** вносит вклад в асимптотику времени в размере **K** (длина строки), но К ограничено задачей в диапазоне от **0** до **200** (можно считать константной). По памяти мы потратим **O**(**1**) (или **O**(**K**)).

## Код:
```python
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = "0" * 201

        for i in strs:
            if len(i) < len(prefix):
                prefix = i

        for word in range(len(strs)):
            word = strs[word]
            for i in range(min(len(word), len(prefix))):
                if word[i] != prefix[i]:
                    prefix = prefix[:i]
                    break
        return prefix


if __name__ == "__main__":
    s = Solution()
    print(s.longestCommonPrefix(["flower", "flow", "flight"]))
    print(s.longestCommonPrefix(["dog", "racecar", "car"]))

```

