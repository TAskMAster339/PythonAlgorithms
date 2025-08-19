<div align='center'>
<h1><a href='https://leetcode.com/problems/plus-one/description/'><strong>132) Plus One</strong></a></h1>
</div>

## **Условие:**

Дано большое число, которое представлено в виде массива цифр **digits**, где **digits**[**i**] представляет собой **i**-тую цифру большого числа. Цифры отсортированы в порядке от самой значащей до самой незначащей цифры слева направо. У большого числа нет незначащих нулей.

Необходимо инкрементировать данное число и вернуть новый массив цифр

## **Идея:**

Ну тут только таблица сложения поможет

## **Реализация:**

Сначала добавим единицу к последней цифре, если получилось переполнение, то есть перенос не равен **0**, то в цикле продолжаем добавлять перенос уже к следующей цифре. И так далее. В конце, если получиться так, что у нас все цифры были переполнены, то нам нужно добавить новый разряд, тогда возвращаем [**1**, ***digits**] (То же самое, что [**1**] + **digits**, где + означает конкатенацию списков). В ином случае просто возвращаем **digits**.



## **Оценка:**

Сложность по времени будет **O**(**N**), где **N** - длина списка **digits**.

Сложность по памяти будет **O**(**1**), так как мы делаем все операции на месте.

## Код:
```python
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        i = len(digits) - 1
        carry = (digits[i] + 1) // 10
        digits[i] = (digits[i] + 1) % 10
        i -= 1
        while carry and i >= 0:
            carry = (digits[i] + 1) // 10
            digits[i] = (digits[i] + 1) % 10
            i -= 1
        if carry:
            return [1, *digits]
        return digits


if __name__ == "__main__":
    f = Solution().plusOne
    print(f([1, 2, 3]))  # [1, 2, 4]
    print(f([4, 3, 2, 1]))  # [4, 3, 2, 2]
    print(f([9]))  # [1, 0]

```

<div align='center'><h3><a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/131.Palindrome%20Number'>⬅️ предыдущая задача</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/README.md'>Все задачи</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/133.Factorial%20Trailing%20Zeroes'>следующая задача ➡️</a></h3></div>