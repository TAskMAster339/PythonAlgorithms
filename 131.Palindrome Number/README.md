<div align='center'>
<h1><a href='https://leetcode.com/problems/palindrome-number/description/'><strong>131) Palindrome Number</strong></a></h1>
</div>

## **Условие:**

Дано число **x**, необходимо вернуть **True**, если оно является палиндромом, иначе **False**.

Палиндром - число, которое одинаково читается как слева направо, так и справа налево

## **Идея:**

Вспомнить полную форму записи числа

## **Реализация:**

Любое число можно представить в полной форме, например, число **123** = **1** * **10**^**2** + **2** * **10**^**1** + **3** * **10**^**0**. Для решения задачи нам нужно развернуть число **x**. Сделаем это с помощью цикла, будем каждую итерацию добавлять сдвигать новое число на **10** и добавлять последнюю цифру **x**. Затем сдвигать **x** на **10**.

После того, как мы вычислим развернутое число, остается вернуть **True**, если **x** == **reversed_x**, иначе **False**.



## **Оценка:**

Сложность по времени будет **O**(**log10** (**X**)), где **X** - данно нам число. **floor**(**log10** (**X**) + **1**) - количество десятичных цифр в числе **X**.

Сложность по памяти будет **O**(**1**).

## Код:
```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        reversed_x = 0
        x_copy = x
        while x:
            reversed_x = reversed_x * 10 + x % 10
            x //= 10
        return x_copy == reversed_x


if __name__ == "__main__":
    f = Solution().isPalindrome
    print(f(121))  # True
    print(f(-121))  # False
    print(f(10))  # False

```

<div align='center'><h3><a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/130.Bitwise%20AND%20of%20Numbers%20Range'>⬅️ предыдущая задача</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/README.md'>Все задачи</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/132.Plus%20One'>следующая задача ➡️</a></h3></div>