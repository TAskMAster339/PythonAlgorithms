<div align='center'>
<h1><a href='https://leetcode.com/problems/zigzag-conversion/description/'><strong>22) Zigzag Conversion</strong></a></h1>
</div>

## **Условие:**

Дана строка, которую нужно представить в виде зигзага. Например, "**PAYPALISHIRING**"

**P**         **A**         **H**         **N**

**A**    **P**    **L**    **S**    **I**    **I**    **G**

**Y**         **I**         **R**

Затем читаем полученный зигзаг по строкам, конкатенируя эти строки, получим ответ. ("**PAHNAPLSIIGYIR**") Нужно написать функцию, которая принимает строку **s**, и количество строк **numRows**, выполняющую вышеописанный алгоритм.

## **Идея:**

Сформировать строки, затем объединить их в искомый результат.

## **Реализация:**

Создадим массив пустых строк **strings**, длинной **numRows**. создадим **count**, в которой будем считать индекс массива **strigns**, по которому лежит строка, в которую мы будем добавлять букву. Также понадобится булева переменная для определения направления зигзага. **Count** будет считать так **0** **1** **2** **3** **2** **1** **0** **1** **2** **3** и так далее. То есть сначала мы идем снизу вверх, пока **up_flag** == **True**, затем, когда **up_flag** == **False**, спускаемся сверху вниз.

Теперь в цикле, который идет по всем буквам в строке. Если мы идем вверх (**up_flag** == **True**), мы добавляем букву в строку **strings**[**count**], инкрементируем **count**. Как только **count** станет больше или равен, чем **numRows**, мы опускаем **up_flag**, и вычитаем **2** из **count**. (**1** раз мы зря прибавили, другой раз нужно вычесть, потому что максимальный индекс нашего массива равен **numRows** - **1**). Аналогично переписываем этот код, если **up_flag** == **False**, меняем + на - и в условии проверяем **count** <= -**1**.

В конце мы получим массив строк, если бы мы записали число, в виде зигзага. Остается с помощью метода .**join**() объединить их в одну строку, которою мы возвращаем.

## **Оценка:**

По времени мы затратим **O**(**N**) (один цикл **for** по всей входной строке длинной **N**). По памяти, мы потратим то же **O**(**N**) (В массиве будут храниться все символы входной строки).

## Код:
```python
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        strings = [""] * numRows
        count = 0
        up_flag = True

        for char in s:
            if up_flag:
                strings[count] += char
                count += 1
                if count >= numRows:
                    up_flag = False
                    count -= 2
            else:
                strings[count] += char
                count -= 1
                if count <= -1:
                    up_flag = True
                    count += 2
        return "".join(strings)


if __name__ == "__main__":
    s = Solution()
    print(s.convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR")
    print(s.convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI")
    print(s.convert("A", 1) == "A")

```

<div align='center'><h3><a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/21.Reverse%20Words%20in%20a%20String'>⬅️ предыдущая задача</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/README.md'>Все задачи</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/23.Find%20the%20Index%20of%20the%20First%20Occurrence%20in%20a%20String'>следующая задача ➡️</a></h3></div>