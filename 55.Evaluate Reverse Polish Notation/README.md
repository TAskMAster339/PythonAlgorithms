<div align='center'>
<h1><a href='https://leetcode.com/problems/evaluate-reverse-polish-notation/description/'><strong>55) Evaluate Reverse Polish Notation</strong></a></h1>
</div>

## **Условие:**

Дан массив строк **tokens**, который представляет собой арифметическое выражение, представленное в постфиксной записи (в обратной польской нотации). Нужно вычислить данное выражение и вернуть число, его значение.

Например:

**3** * (**2** + **3**) = **15** - классическая запись

**2** **3** + **3** * = **15** - постфиксная запись (обратная польская нотация)

## **Идея:**

Для подсчета постфиксной записи используется стек

## **Реализация:**

Всё просто. Если элемент массива число, то мы просто кладем его в стек. Если элемент знак операции (+-/*), то мы достаем два элемента из массива и выполняем с ними соответствующую операцию. Результат этой операции записываем в стек.

В конце у нас в стеке останется одно число, а именно результат математического выражения.

Пример:

**2** **3** + **3** *

**2** + **3** = **5**;  **5** **3** *

**5** * **3** = **15**;  **15**

Ответ: **15**



## **Оценка:**

По времени мы затратим **O**(**N**), по памяти **O**(**1**).

## Код:
```python
from typing import List
from util import test_case as tc


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            if i in "+-*/":
                elem2 = stack.pop()
                elem1 = stack.pop()
                match i:
                    case "+":
                        stack.append(elem1 + elem2)
                    case "-":
                        stack.append(elem1 - elem2)
                    case "*":
                        stack.append(elem1 * elem2)
                    case "/":
                        stack.append(int(elem1 / elem2))
            else:
                stack.append(int(i))
        return stack[0]


if __name__ == "__main__":
    f = Solution().evalRPN
    tc(f, 9, tokens=["2", "1", "+", "3", "*"])
    tc(f, 6, tokens=["4", "13", "5", "/", "+"])
    tc(
        f,
        22,
        ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"],
    )
    tc(f, -7, ["4", "-2", "/", "2", "-3", "-", "-"])

```

<div align='center'><h3><a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/54.Min%20Stack'>⬅️ предыдущая задача</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/README.md'>Все задачи</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/56.Basic%20Calculator'>следующая задача ➡️</a></h3></div>