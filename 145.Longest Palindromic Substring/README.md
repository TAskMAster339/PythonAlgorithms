<div align='center'>
<h1><a href='https://leetcode.com/problems/longest-palindromic-substring/description/'><strong>145) Longest Palindromic Substring</strong></a></h1>
</div>

## **Условие:**

Дана строка **s**, необходимо вернуть наибольшую подстроку, которая является палиндромом.

Строка **s** является палиндромом, если **s** = **s**[::-**1**]

## **Идея:**

Заметим, что проще всего палиндром проверять с центра к краям

## **Реализация:**

Пройдемся циклом по каждой букве в **s**, так как она потенциально является центром какого-то полинома. Будем идти влево и вправо одновременно от этой буквы до тех пор, пока **s**[**start**] == **s**[**end**]. Единственное, что стоит учесть - палиндром может быть как четным по длине, так и не четным, то есть середины будет разная. Поэтому будем проверять каждую букву как середину двух палиндромов: четного и нечетного.

Как только эти буквы начнут различаться, то мы нашли претендента на наибольшего палиндрома. Записываем в **result**, наибольший палиндром, чтобы в конце вернуть его.



## **Оценка:**

По времени в наихудшем случае мы затратим **O**(**N**^**2**), где **N** - длина строки **s**.

По памяти мы затратим **O**(**1**).

## Код:
```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""

        for i in range(len(s)):
            start, end = i, i

            while end < len(s) and start > -1 and s[start] == s[end]:
                start -= 1
                end += 1

            longest = s[start + 1 : end]
            if len(longest) > len(result):
                result = longest

            start, end = i, i + 1

            while end < len(s) and start > -1 and s[start] == s[end]:
                start -= 1
                end += 1

            longest = s[start + 1 : end]
            if len(longest) > len(result):
                result = longest

        return result


if __name__ == "__main__":
    f = Solution().longestPalindrome
    print(f("babad"))  # "bab"
    print(f("cbbd"))  # "bb"

```

<div align='center'><h3><a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/144.Unique%20Paths%20II'>⬅️ предыдущая задача</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/README.md'>Все задачи</a></h3></div>