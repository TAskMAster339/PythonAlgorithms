<div align='center'>
<h1><a href='https://leetcode.com/problems/single-number-ii/description/'><strong>129) Single Number II</strong></a></h1>
</div>

## **Условие:**

Дан массив целых чисел **nums**, в котором каждый элемент, кроме одного, встречается три раза, нужно вернуть этот единственный элемент

## **Идея:**

Нужно обобщить идею предыдущей задачи

## **Реализация:**

Немного улучшим предыдущую идею. Её проблема в том, что при **XOR** **3** одинаковых чисел мы не получаем **0**. Это легко поправить, если создать две переменные **ones** и **twos**. **C** помощью данных переменных мы будем помечать единицей те позиции, которые мы встречали один или два раза единицу соответственно. В итоге, если число встречается три раза, то все его позиции единиц в двоичном представлении будут в соответствующих позициях **ones** и **twos** равны **0**. Таким образом число, которое встречается ровно один раз в конце алгоритма будет записано в **ones**.



## **Оценка:**

Сложность по времени **O**(**N**), где **N** - длина массива **nums**.

Сложность по памяти **O**(**1**).

## Код:
```python
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        ones = 0
        twos = 0
        for num in nums:
            ones ^= num & ~twos
            twos ^= num & ~ones
        return ones


if __name__ == "__main__":
    f = Solution().singleNumber
    print(f([2, 2, 3, 2]))  # 3
    print(f([0, 1, 0, 1, 0, 1, 99]))  # 99

```

<div align='center'><h3><a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/128.Single%20Number'>⬅️ предыдущая задача</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/README.md'>Все задачи</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/130.Bitwise%20AND%20of%20Numbers%20Range'>следующая задача ➡️</a></h3></div>