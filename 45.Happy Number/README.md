<div align='center'>
<h1><a href='https://leetcode.com/problems/happy-number/description/'><strong>45) Happy Number</strong></a></h1>
</div>

## **Условие:**

Нужно написать алгоритм, который определяет является ли число **n** "счастливым".

"Счастливое" число определяется по следующим признакам:

**1**) **n** - натуральное число

**2**) строим следующие число, которое равно сумме квадратов цифр числа **n**

**3**) повторяем до тех пор, пока не получим **1**.

**4**) если мы получили **1**, то число счастливое

Нужно вернуть **True**, если число счастливое, **False**, если мы попали в бесконечный цикл.

## **Идея:**

Нужно как-то пройти ровно один раз по этому циклу, затем просто посмотреть была ли где-то в нем единица.

## **Реализация:**

Создадим словарь **table**, затем в бесконечном цикле будем выполнять пункты **2**) и **3**), заполняя наш словарь. Как только мы нашли ключ, который уже есть в словаре, мы понимаем, что мы зациклились, выходим из цикла. В конце мы проверяем: встретили ли мы единицу, если встретили, то возвращаем **True**, иначе **False**.



## **Оценка:**

По времени мы затратим **O**(**K**), где **K** - количество итераций в цикле (длина цикла, полученного пунктами **2**) и **3**)), по памяти мы затратим тоже **O**(**K**), потому что будем хранить каждую итерацию цикла.

## Код:
```python
from util.test import test_case


class Solution:
    def isHappy(self, n: int) -> bool:
        table = dict()

        while True:
            tmp = 0
            while n > 0:
                tmp += (n % 10) ** 2
                n //= 10
            if tmp in table:
                break
            else:
                table[tmp] = 1
            n = tmp

        return any(x == 1 for x in table.keys())


if __name__ == "__main__":
    f = Solution().isHappy
    test_case(f, True, 19)
    test_case(f, False, 2)

```

<div align='center'><h3><a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/44.Two%20Sum'>⬅️ предыдущая задача</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/README.md'>Все задачи</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/46.Contains%20Duplicate%20II'>следующая задача ➡️</a></h3></div>