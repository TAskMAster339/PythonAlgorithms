<div align='center'>
<h1><a href='https://leetcode.com/problems/group-anagrams/description/'><strong>43) Group Anagrams</strong></a></h1>
</div>

## **Условие:**

Дан массив строк **strs**, нужно сгруппировать эти строки в массивы анаграмм.

## **Идея:**

Проще всего воспользоваться сортировкой.

## **Реализация:**

Создадим словарь **result**. Пройдемся по строкам в массиве, будем сортировать каждую строку в алфавитном порядке. Отсортированная строка будет ключом в нашей хэш-таблице, а значением будет массив строк. Все строки в этом массиве будут анаграммами. В конце нужно вернуть массив всех значений нашей хэш-таблицы.



## **Оценка:**

Верхняя асимптотическая граница по времени равна **O**(**N**), так как мы перебираем **N** слов. (Сортировка строки происходит за **O**(**K**), но в нашей задаче **K**=**100**, поэтому временем сортировки можно пренебречь). По памяти мы тратим **O**(**N**), так как нам придется хранить все **N** слов.

## Код:
```python
from typing import List
from util import test_case


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []

        i = 0
        index = 0
        while i < len(strs):
            if strs[i] == "000":
                i += 1
                continue
            etalon = dict()
            word = strs[i]

            for char in word:
                if char in etalon:
                    etalon[char] += 1
                else:
                    etalon[char] = 1
            result.append([word])
            strs[i] = "000"
            for j in range(i + 1, len(strs)):
                if strs[j] == "000" or len(strs[j]) != len(word):
                    continue
                table = dict()
                other_word = strs[j]

                for char in other_word:
                    if char in table:
                        table[char] += 1
                    else:
                        table[char] = 1

                if table == etalon:
                    result[index].append(other_word)
                    strs[j] = "000"
            i += 1
            index += 1
        return result

    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        result = dict()

        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in result:
                result[sorted_word].append(word)
            else:
                result[sorted_word] = [word]

        return list(result.values())


if __name__ == "__main__":
    s = Solution().groupAnagrams2
    test_case(
        s,
        [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]],
        ["eat", "tea", "tan", "ate", "nat", "bat"],
    )
    test_case(s, [[""]], [""])
    test_case(s, [["a"]], ["a"])

```

<div align='center'><h3><a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/42.Valid%20Anagram'>⬅️ предыдущая задача</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/README.md'>Все задачи</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/44.Two%20Sum'>следующая задача ➡️</a></h3></div>