<div align='center'>
<h1><a href='https://leetcode.com/problems/word-break/description/'><strong>139) Word Break</strong></a></h1>
</div>

## **Условие:**

Дана строка **s** и массив строк **wordDict**, нужно вернуть **True**, если строку **s** можно представить в виде слов из **wordDict**. При этом одно и то же слово может быть использовано несколько раз

## **Идея:**

Создадим массив **dp**, в котором **dp**[**i**] будет **True**, если мы можем представить строку **s**[:**i**+**1**] через слова из **wordDict**, иначе **False**

## **Реализация:**

Создадим массив **dp**, состоящий из **False**. Первое значение будет **True**.

Затем пройдемся циклом по буквам строки **s**. И для каждой **i**-той буквы будем проверять есть ли слово **s**[**start**:**i**] в списке **wordDict**.

**start** - это потенциально возможный индекс начала слова из **wordDict**, который вычисляется вот так: **i** - **len**(**wordFromDict**).

Также важным условием является то, что слова должны идти друг за другом. То есть мы должны проверять, что **dp**[**start**] == **True**, это условие проверяют, что эти слова идут подряд, то есть не возникнет вот таких случаев ("**dogscat**", ["**dog**", "**cat**"], **dp**[**index**(**s**)] == **False**, что значит, что мы не можем представить строку "**dogscat**" через данные нам слова).



## **Оценка:**

Сложность по времени будет **O**(**N** * **K**), где **N** - длина строки **s**, **K** - количество слов в **wordDict**.

Сложность по памяти будет **O**(**N**), размер массива **dp**.

## Код:
```python
class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        dp = [True] + [False] * len(s)

        for i in range(1, len(s) + 1):
            for w in wordDict:
                start = i - len(w)
                if start >= 0 and dp[start] and s[start:i] == w:
                    dp[i] = True
                    break

        return dp[-1]


if __name__ == "__main__":
    f = Solution().wordBreak
    print(f("leetcode", ["leet", "code"]))  # True
    print(f("applepenapple", ["apple", "pen"]))  # True
    print(f("catsandog", ["cats", "dog", "sand", "and", "cat"]))  # False
    print(f("aaaaaaa", ["aaaa", "aaa"]))  # True

```

<div align='center'><h3><a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/138.House%20Robber'>⬅️ предыдущая задача</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/README.md'>Все задачи</a></h3></div>