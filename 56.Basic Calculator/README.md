<div align='center'>
<h1><a href='https://leetcode.com/problems/basic-calculator/description/'><strong>56) Basic Calculator</strong></a></h1>
</div>

## **Условие:**

Дана строка **s**, которая представляет собой корректное математическое выражение, нужно реализовать базовый калькулятор, чтобы вычислить его. Нужно вернуть результат выражения.

Строка **s** состоит из чисел и символов "+-( )".

## **Идея:**

Нужно преобразовать данное выражение в постфиксную запись, затем мы уже знаем, что делать.

## **Реализация:**

Для решение этой задачи воспользуемся алгоритмом Дейкстры. В начале преобразуем данную строку: уберем пробелы, также с помощью регулярных выражений я заменил все унарные минусы на бинарные. (-**5** = **0** - **5**) (Можно сделать и по другому)

Еще создадим стек операций.

Алгоритм следующий:

**1**) Если мы встречаем число, то мы записываем его в конец постфиксной записи.

**2**) Если мы встречаем знак, то мы, во-первых, достаем из стека все операции с таким же или более высоким приоритетом (* > +), записываем их в постфиксную запись. Во-вторых, добавляем этот оператор в стек.

**3**) Если мы встретили открывающую скобку, то мы добавляем её в стек.

**4**) Если мы встретили закрывающую скобку, то мы достаем элементы из стека и добавляем их постфиксную запись до тех пор, пока не найдем открывающую скобку.

**5**) В конце, если стек оказался не пустым, то мы достаем оттуда все элементы и записываем их в постфиксную запись.

В итоге мы получим обратную польскую нотацию. Считаем её так, как уже умеем. Возвращаем результат.



## **Оценка:**

Верхняя граница по времени будет **O**(**N**), где **N** - длина строки. По памяти оценка будет **O**(**N**), память уходит на хранение постфиксной записи.

## Код:
```python
from util import test_case
from typing import List
import re


def evalRPN(tokens: List[str]) -> int:
    stack = []

    for i in tokens:
        if i in "+-":
            elem2 = stack.pop()
            elem1 = stack.pop()
            match i:
                case "+":
                    stack.append(elem1 + elem2)
                case "-":
                    stack.append(elem1 - elem2)
        else:
            stack.append(int(i))
    return stack[0]


class Solution:
    def calculate(self, s: str) -> int:
        RPN = []
        stack = []

        number = ""
        s = s.replace(" ", "")
        if s[0] == "-":
            s = "0" + s
        s = re.sub(r"\(-(\d+)", r"(0-\1", s)
        s = re.sub(r"\(-\(", r"(0-(", s)
        for i in range(len(s)):
            char = s[i]

            if char.isnumeric():
                number += char
            else:
                if number:
                    RPN.append(number)
                number = ""
                if char == "(":
                    stack.append(char)
                elif char == ")":
                    while stack and stack[-1] != "(":
                        RPN.append(stack.pop())
                    stack.pop()
                elif char in "+-":
                    while stack and stack[-1] in "+-":
                        RPN.append(stack.pop())
                    stack.append(char)
        if number:
            RPN.append(number)
        for item in reversed(stack):
            RPN.append(item)

        return evalRPN(RPN)


if __name__ == "__main__":
    f = Solution().calculate
    test_case(f, 2, s="1 + 1")
    test_case(f, 3, s=" 2-1 + 2 ")
    test_case(f, 23, s="(1+(4+5+2)-3)+(6+8)")
    test_case(f, 3, "1-(     -2)")
    test_case(f, -12, "- (3 - (- (4 + 5) ) )")

```

<div align='center'><h3><a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/55.Evaluate%20Reverse%20Polish%20Notation'>⬅️ предыдущая задача</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/README.md'>Все задачи</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/57.Linked%20List%20Cycle'>следующая задача ➡️</a></h3></div>