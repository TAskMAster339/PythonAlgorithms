<div align='center'>
<h1><a href='https://leetcode.com/problems/min-stack/description/'><strong>54) Min Stack</strong></a></h1>
</div>

## **Условие:**

Нужно спроектировать стек, который поддерживает операции **push**, **pop**, **top**, **getMin**, которая возвращает минимальный элемент в стеке.

Верхняя граница по времени у всех методов должна быть **O**(**1**).

## **Идея:**

Как-то достичь **O**(**1**).

## **Реализация:**

Есть два способа:

**1**) Мы будем динамически вычислять минимальный элемент при добавлении в стек. Единственный сложный момент это при удалении элемента, тогда есть вероятность удаления минимума. Если мы удаляем минимум, то нам нужно будет заново пересчитать минимум в массиве.

**2**) Будем сохранять пары значений [**val**, **min_val**], где **min_val** будет минимальным значением последовательности всех элементов от начала стека до данного элемента, включая его. Например, стек [**2** **4** **1**] -> [(**2**, **2**), (**4**, **2**), (**1**, **1**)]. Таким образом мы всегда можем получить минимальный элемент.



## **Оценка:**

**1**) Верхняя граница по времени будет **O**(**1**). Она получается с помощью амортизационного анализа. В наихудшем случае у нас будет **N**, элементов в стеке, тогда при удалении минимума из массива мы затратим **O**(**N**) (поиск минимума). Но вероятность попасть в такую ситуацию **1**/**N**. При больших **N** она стремится к **0**, при малых поиск минимума можно считать константным. Поэтому при малых **N** оценка по времени **O**(**1**), при больших **1**/**N** * **O**(**N**) = **O**(**1**).

По памяти **O**(**N**)

**2**) Здесь очевидно по времени **O**(**1**), но по памяти мы затратим в два раза больше, хотя будет то же самое **O**(**N**) = **O**(**2*****N**).

## Код:
```python
class MinStackNoMemo:
    def __init__(self):
        self.data = []
        self.min = float("inf")

    def push(self, val: int) -> None:
        self.data.append(val)
        if val < self.min:
            self.min = val

    def pop(self) -> None:
        elem = self.data.pop()
        if elem == self.min:
            if self.data:
                self.min = min(self.data)
            else:
                self.min = float("inf")

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.min


class MinStack:
    def __init__(self):
        self.data = []

    def push(self, val: int) -> None:
        if not self.data:
            self.data.append((val, val))
        else:
            self.data.append((val, min(val, self.data[-1][0])))

    def pop(self) -> None:
        self.data.pop()

    def top(self) -> int:
        return self.data[-1][0]

    def getMin(self) -> int:
        return self.data[-1][1]


if __name__ == "__main__":
    obj = MinStack()
    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    print(obj.getMin())
    obj.pop()
    print(obj.top())
    print(obj.getMin())

```

<div align='center'><h3><a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/53.Simplify%20Path'>⬅️ предыдущая задача</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/README.md'>Все задачи</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/55.Evaluate%20Reverse%20Polish%20Notation'>следующая задача ➡️</a></h3></div>