<div align='center'>
<h1><a href='https://leetcode.com/problems/add-binary/description/'><strong>125) Add Binary</strong></a></h1>
</div>

## **Условие:**

Даны две строки **a** и **b**, которые представляют собой бинарные числа, нужно вернуть строку, которая представляет собой их сумму

## **Идея:**

Вспомнить как складываются бинарные числа

## **Реализация:**

Создадим два указателя, которые будут указывать на две первые цифры числа (последние символы строки). Создадим переменную **carry**, в которой будем считать перенос и массив **result**, который будем заполнять суммами цифр.

В цикли пока или один из указателей или другой больше или равен **0**, мы будем считать сумму цифры из первого числа, цифры из второго числа и переноса. В **result** будем добавлять остаток от суммы при делении на **2**. В перенос будем записывать сумму разделенную нацело на **2**.

Остаётся корректно обработать те случаи, когда одно из чисел закончилось. В данном случае делаем всё то же самое, только сумму считаем без одного из слагаемых.

Также в конце надо не забыть про то, что перенос может остаться равным **1**, необходимо в этом случае добавить еще одну единицу в массив. В конце мы возвращаем строку составленную из чисел инвертированного массива. (Инвертировать надо так как мы складывали числа справа налево, а записывались они в массив слева направо).



## **Оценка:**

Сложность по времени будет **O**(**max**(**N**, **K**)), где **N**, **K** - длины строк **a** и **b** соответственно.

Сложность по памяти будет **O**(**1**), так как мы не используем дополнительной памяти.

## Код:
```python
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        result = []
        while i >= 0 or j >= 0:
            if i < 0:
                summary = int(b[j]) + carry
                carry = summary // 2
                result.append(str(summary % 2))
                j -= 1
            elif j < 0:
                summary = int(a[i]) + carry
                carry = summary // 2
                result.append(str(summary % 2))
                i -= 1
            else:
                summary = int(a[i]) + int(b[j]) + carry
                carry = summary // 2
                result.append(str(summary % 2))
                i -= 1
                j -= 1
        if carry:
            result.append("1")
        return "".join(reversed(result))


if __name__ == "__main__":
    f = Solution().addBinary
    print(f("11", "1"))  # "100"
    print(f("1010", "1011"))  # "10101"

```

<div align='center'><h3><a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/124.Find%20Median%20from%20Data%20Stream'>⬅️ предыдущая задача</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/README.md'>Все задачи</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/126.Reverse%20Bits'>следующая задача ➡️</a></h3></div>