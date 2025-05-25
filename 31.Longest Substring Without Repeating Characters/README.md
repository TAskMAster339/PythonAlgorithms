<div align='center'>
<h1><a href='https://leetcode.com/problems/longest-substring-without-repeating-characters/description/'><strong>31) Longest Substring Without Repeating Characters</strong></a></h1>
</div>

## **Условие:**

Дана строка **s**, нужно найти длину наибольшей подстроки, в которой все символы уникальны.

Подстрока - непрерывная непустая последовательность символов в строке.

## **Идея:**

Уникальные символы намекают на множество

## **Реализация:**

Если строка имеет длину <= **1**, то мы возвращаем саму длину. Теперь, когда мы обработали крайний случай, создадим переменную **max_len** для подсчета максимальной длины подстроки. Указатель **start**, который будет использоваться для подсчета длины максимальной подстроки. Также множество **letter_set**.

Теперь с помощью цикла пройдемся по символам строки. Если символ не в множестве, то мы его туда добавляем, при этом пересчитывая **max_len**. Если символ есть в множестве, то мы удаляем все предыдущие символы **s**[**start**] до тех пор, пока не сможем добавить символ в множество.

После цикла возвращаем **max_len**.



## **Оценка:**

Множество размером **M** обычно реализуется каким-либо бинарным деревом поиска, в котором все операции выполняются за **O**(**log** **M**) по времени, каждую итерацию цикла длинной **N** мы будем выполнять как минимум одну такую операцию, поэтому сложность в наихудшем случае будет **O**(**N** * **log** **M**). Но так как символы - элементы английского алфавита + цифры + пробел, получим **M** = **37**, следовательно **O**(**6**.**1** * **N**), что равно **O**(**N**). По памяти мы потратим **O**(**M**), так как в наихудшем случае мы будем хранить весь алфавит. Но так как **M** много меньше по сравнению с **N**, то итоговая граница будет **O**(**1**).

## Код:
```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        max_len = 0
        start = 0
        letter_set = {s[start]}

        for end in range(1, len(s)):
            while s[end] in letter_set:
                letter_set.remove(s[start])
                start += 1
            else:
                letter_set.add(s[end])
                max_len = max(max_len, end - start + 1)

        return max_len


if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb"))
    print(s.lengthOfLongestSubstring("bbbbb"))
    print(s.lengthOfLongestSubstring("pwwkew"))
    print(s.lengthOfLongestSubstring(" "))

```

<div align='center'><h3><a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/30.Minimum%20Size%20Subarray%20Sum'>⬅️ предыдущая задача</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/README.md'>Все задачи</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/32.Substring%20with%20Concatenation%20of%20All%20Words'>следующая задача ➡️</a></h3></div>