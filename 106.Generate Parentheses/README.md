<div align='center'>
<h1><a href='https://leetcode.com/problems/generate-parentheses/description/'><strong>106) Generate Parentheses</strong></a></h1>
</div>

## **Условие:**

Дано **n** пар скобочек, нужно создать функцию, которая сгенерирует все возможные комбинации из **n** пар скобочек корректных скобочных последовательностей

## **Идея:**

Построить дерево скобочек, где каждая путь от корня до листа дает корректную скобочную последовательность

## **Реализация:**

Построив дерево, нам останется построить функцию, которая будет делать обход от корня до листа. С помощью **backtracking** будем оптимизировать это.

Создадим функцию **backtrack**, которая будет создавать нашу последовательность. Для этого нам понадобится считать количество открытых скобок (Можно считать количество закрытых, но мы его легко можем вычислить с помощью количества открытых скобок)

Крайний случай - когда длина нашей последовательности стала **2** * **n**, тогда записываем её в **result**.

Рекуррентный случай - мы пойдем по следующей логике:

**1**) Сначала мы будем пытаться добавлять открывающие скобки до максимума, то есть до **n**. Важно это делать до добавление закрывающих скобок.

**2**) Затем мы будем добавлять до талого закрывающие скобки, при условии, что закрытие в данный момент корректно, закрытие корректно тогда, когда количество открытых скобок больше количества закрытых.

В конце обоих действий мы делаем откат. Таким образом мы составим все корректные скобочные последовательности.



## **Оценка:**

По времени наш алгоритм оценить очень сложно. Для этого необходимо узнать про числа Каталана. Число Каталана **C_n** = (**2n**)! / ((**n**+**1**)! * **n**!) обозначает количество правильных скобочных последовательностей из **n** пар скобок. Её асимптотика равна **C_N** = **4**^**N** / (**N**^(**3**/**2**) * **sqrt**(**PI**)).

Наш алгоритм посчитает все числа Каталана, при этом еще на каждое число будет потрачено **O**(**N**) времени на сохранение в **result**. Итого, верхняя граница по времени будет **O**(**N** * **4**^**N** / (**N**^(**3**/**2**))) = **O**(**4**^**N** / **sqrt**(**N**))

Верхняя граница по памяти будет **O**(**N**), просто расходы на стек вызовов функций.

## Код:
```python
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []
        comb = []

        def backtrack(num: int, comb: list[str]):
            if len(comb) == 2 * n:
                result.append("".join(comb))
                return

            if num < n:
                comb.append("(")
                backtrack(num + 1, comb)
                comb.pop()
            if num * 2 != len(comb):
                comb.append(")")
                backtrack(num, comb)
                comb.pop()

        backtrack(0, comb)
        return result


if __name__ == "__main__":
    f = Solution().generateParenthesis
    print(f(3))
    print(f(1))

```

<div align='center'><h3><a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/105.N-Queens%20II'>⬅️ предыдущая задача</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/README.md'>Все задачи</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/107.Word%20Search'>следующая задача ➡️</a></h3></div>