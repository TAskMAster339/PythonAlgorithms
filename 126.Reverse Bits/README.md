<div align='center'>
<h1><a href='https://leetcode.com/problems/reverse-bits/description/'><strong>126) Reverse Bits</strong></a></h1>
</div>

## **Условие:**

Дано положительное чётное число, которое можно уместить в **32**-ух битах. Необходимо инвертировать его и вернуть полученное число

## **Идея:**

Задача проще простого, но интерес в том, чтобы оптимизировать до никуда

## **Реализация:**

Для лучшего понимания смотрите картинку. Мы создадим число **result**, которое и вернём. Будем с помощью битовых операций добавлять к нему по одной последней цифре. С помощью сдвига влево мы будем двигать **result** и с помощью дизъюнкции и конъюнкции добавлять первое число в данном. Затем с помощью битового сдвига вправо мы будем двигать данное число.



## **Оценка:**

Сложность по времени будет **O**(**1**), так как всего у нас будет **32** итерации в цикле, то есть никак не зависит от размера числа **N**.

Сложность по памяти **O**(**1**).

## Код:
```python
class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for _ in range(32):
            result = (result << 1) | (n & 1)
            n >>= 1
        return result


if __name__ == "__main__":
    f = Solution().reverseBits
    print(f(43261596))  # 964176192
    print(f(2147483644))  # 1073741822

```

<div align='center'><h3><a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/125.Add%20Binary'>⬅️ предыдущая задача</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/README.md'>Все задачи</a></h3></div>