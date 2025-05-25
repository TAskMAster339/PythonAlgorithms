# [**39) Ransom Note**](https://leetcode.com/problems/ransom-note/description/)

## **Условие:**

Дано две строки **ransomNote** и **magazine**, нужно вернуть **True**, если **ransomNote** может быть составлена из букв строки **magazine**, иначе **False**.

## **Идея:**

Подсчитать частоту букв в словах.

## **Реализация:**

Создадим словарь **table**, в который запишем частоту букв строки **magazine**.

После этого пройдемся по всем буквам строки **ransomNote**, будем проверять каждую букву на следующие условия:

**1**) Есть ли она в нашей таблице, если нет возвращаем **False**

**2**) Если она есть в нашей таблице, но её частота равно **0**, то тоже возвращаем **False**.

**3**) Если выше упомянутые условия не выполнились убавим частоту этой буквы на **1**.

Если мы не вернули **False** в цикле, то это значит, что у нас достаточно букв, возвращаем **True**.



## **Оценка:**

По времени оценка будет **O**(**1**) (Так как каждый цикл проходит по буквам в строке, а их у нас ограниченное количество, и обращение к хэш-таблице происходит за константное время). По памяти мы получим тоже **O**(**1**), по тем же причинам.

## Код:
```python
from util import test_case


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        table = dict()
        for letter in magazine:
            if letter in table:
                table[letter] += 1
            else:
                table[letter] = 1

        for letter in ransomNote:
            if letter not in table.keys():
                return False
            if table[letter] == 0:
                return False
            table[letter] -= 1

        return True


if __name__ == "__main__":
    s = Solution()
    test_case(s.canConstruct, False, "a", "b")
    test_case(s.canConstruct, False, "aa", "ab")
    test_case(s.canConstruct, True, "aa", "aab")

```

### [<-- предыдущая задача](https://github.com/TAskMAster339/PythonAlgorithms/tree/main/38.Game%20of%20Life) | [следующая задача -->](https://github.com/TAskMAster339/PythonAlgorithms/tree/main/40.Isomorphic%20Strings)
