# [**25) Valid Palindrome**](https://leetcode.com/problems/valid-palindrome/description/)

## **Условие:**

Фраза является палиндромом, если после превращения всех прописных букв в строчные и удаления всех символов, которые не являются буквами или числами, она читается слева направо, точно также как справа налево. Дана строка **s**, нужно вернуть **True**, если она палиндром, иначе **False**.

## **Идея:**

Самое сложное это подогнать строку под условие палиндрома.

## **Реализация:**

С помощью метода .**lower**() преобразуем все символы к нижнему регистру. Затем создаем строку **result**, в которую запишем только буквы и цифры из строки **s**. Проверять это будем с помощью метода .**isalnum**(). В конце остается сравнить строку с её инвертированной версией. Для этого в **Python** можно воспользоваться срезом [::-**1**] (вся последовательность, только с обратным шагом). Если **result** == **result**[::-**1**], то это палиндром, возвращаем **True**, иначе **False**.



## **Оценка:**

Один проход по строке, и последующая её инверсия даст нам **O**(**N**) асимптотику по времени. По памяти нам понадобиться **O**(**N**) для хранения строки **result**.

## Код:
```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        result = ""
        for char in s:
            if char.isalnum():
                result += char
        return result == result[::-1]


if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome("A man, a plan, a canal: Panama"))
    print(s.isPalindrome("race a car"))
    print(s.isPalindrome(" "))

```

### [<-- предыдущая задача](https://github.com/TAskMAster339/PythonAlgorithms/tree/main/24.Text%20Justification) | [следующая задача -->](https://github.com/TAskMAster339/PythonAlgorithms/tree/main/26.Is%20Subsequence)
