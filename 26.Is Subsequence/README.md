<div align='center'>
<h1><a href='https://leetcode.com/problems/is-subsequence/description/'><strong>26) Is Subsequence</strong></a></h1>
</div>

## **Условие:**

Дано две строки **s** и **t**, нужно вернуть **True**, если **s** является подпоследовательностью **t**, или **False** в ином случае.

Подпоследовательность строки это новая строка, которая получена из оригинальной путем удаления (может быть **0** удалений) символов при этом никак не меняя относительное положение оставшихся символов (Например, "**ace**" подпоследовательность "**abcde**", а "**aec**" нет)

## **Идея:**

Нужно как-то проверить, что все символы строки **s** есть в **t**, при этом их порядок не нарушен.

## **Реализация:**

Вначале проверим крайний случай. Если **s** пустая строка, то возвращаем **True**, так как пустая строка является подпоследовательностью любой строки. Далее создадим переменную **index** = **0**, в которой будем отслеживать **s**[**index**] символ строки **s**. Далее пройдем циклом по всем символам строки **t**. Если символ строки **t** оказался равен **s**[**index**], то мы инкрементируем индекс. Этот процесс происходит до тех пор, пока **index** не станет равным длине строки **s**. Это значит, что в строке **t** присутствуют все символы строки **s**, и они еще при этом расположены в правильном порядке. Значит мы нашли подпоследовательность, возвращаем **True**. После цикла возвращаем **False**, так как подпоследовательность не была найдена.



## **Оценка:**

Так как мы делаем один проход по циклу, то мы потратим **O**(**N**) времени, где **N** - длина строки **t**. По памяти я сильно сэкономил, так как не пытался сохранить найденную подпоследовательность, поэтому затратил **O**(**1**), если бы пытался, то потратил бы **O**(**N**).

## Код:
```python
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True

        index = 0

        for i in range(len(t)):
            char = t[i]
            if index < len(s) and char == s[index]:
                index += 1
            if index == len(s):
                return True

        return False


if __name__ == "__main__":
    s = Solution()
    print(s.isSubsequence("abc", "ahbgdc"))
    print(s.isSubsequence("axc", "ahbgdc"))
    print(s.isSubsequence("acb", "ahbgdc"))
    print(s.isSubsequence("ab", "baab"))
    print(s.isSubsequence("", ""))

```

<div align='center'><h3><a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/25.Valid%20Palindrome'>⬅️ предыдущая задача</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/README.md'>Все задачи</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/27.Two%20Sum%20II%20-%20Input%20Array%20Is%20Sorted'>следующая задача ➡️</a></h3></div>