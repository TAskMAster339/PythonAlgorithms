<div align='center'>
<h1><a href='https://leetcode.com/problems/text-justification/description/'><strong>24) Text Justification</strong></a></h1>
</div>

## **Условие:**

Дан массив строк **words** и ширина **maxWidth**, нужно отформатировать текст таким образом, чтобы каждая строка в нем была длиной в **maxWidth** символов и была выравнена по ширине. В строке должно быть так много слов, насколько возможно. Слова разделяются пробелами. Пробелы в строке распределяются равномерно, если это невозможно, то слева на право. Последняя строка текста должна быть выровнена по левому краю.

## **Идея:**

Нужно реализовать две вещи: **1**) деление слов по строкам, **2**) расстановка пробелов.

## **Реализация:**

**1**) Создадим массив **result**, в который будем записывать строки, состоящий из слов, разделенных одним пробелом. С помощью цикла, пробегающего по всем словам, мы будем пытаться составить самую длинную строку, меньшую чем **maxWidth**, когда добавить еще одно слово в эту строку невозможно, то мы добавляем её в массив **result**. После цикла нужно проверить то, что осталось во временной строке **tmp_string**. Если она не пустая, то добавляем её в конец массива, это будет наша последняя строка.

**2**) Теперь пробегаемся по всем строкам нашего массива **result**, производя выравнивание по ширине. С помощью функции **justify**(**line**, **width**) я выравниваю строку по ширине. Для этого я рассчитываю **2** основных числа, первое число - это количество равномерно распределенных пробелов, второе число - это пробелы, которые надо распределить неравномерно. Например, если у нас есть **2** слова размером по **6** и **7** букв, а **maxWidth**==**16**, то количество пробелов должно быть **16** - **6** - **7** = **3**. Равномерное количество будет равно **1**, также есть один неравномерный пробел, который будет идти после **1** слова (по условию задачи).

Мы преобразуем нашу строку в массив слов, после чего в цикле конкатенируем эти слова с пробелами, учитывая ранее посчитанное количество равномерных и неравномерных пробелов. В конце функция возвращает строку, выравненную по ширине.

Остается особо обработать последнюю строку. В ней все слова разделены одним пробелом и в конце просто дописываем столько пробелов, сколько необходимо для того, чтобы длина строки равнялась **maxWidth**.

В итоге в **result** записан искомый ответ.

## **Оценка:**

По времени мы потратим **O**(**N** * **K**), где **N** - количество слов, **K** - количество слов в одной строке. По условиям задачи **K** будет очень мало, так как оно зависит от **maxWidth** (**maxWidth** ограничено в диапазоне от **1** до **100**), при **maxWidth**, стремящемся к бесконечности, время будет стремится к **O**(**N**^**2**), в нашем случае будет **O**(**N**). По памяти мы будем хранить массив строк, это **O**(**N**), также процедура **justify**, потребует **O**(**N**). Суммарно получим **O**(**N**) затрат по памяти.

## Код:
```python
from typing import List


class Solution:
    def fullJustify(self, strs: List[str], maxWidth: int) -> List[str]:
        result = []
        tmp_string = ""
        length = 0
        for string in strs:
            if len(string) + length > maxWidth:
                result.append(tmp_string.strip())
                tmp_string = string + " "
                length = len(string) + 1
            else:
                tmp_string += string + " "
                length += len(string) + 1
        if tmp_string != "":
            result.append(tmp_string.strip())

        for i in range(len(result)):
            if i != len(result) - 1:
                result[i] = self.justify(result[i], maxWidth)
            else:
                result[i] = result[i] + " " * (maxWidth - len(result[i]))

        return result

    def justify(self, line, width):
        words = line.split(" ")
        space_num = line.count(" ")
        empty = width - (len(line) - space_num)
        full_spaces = empty // space_num if space_num != 0 else empty
        spaces_need_to_add = empty % space_num if space_num != 0 else empty

        if len(words) == 1:
            return words[0] + " " * (width - len(words[0]))
        result = words[0]
        for i in range(1, len(words)):
            if spaces_need_to_add > 0:
                space = " " * (full_spaces + 1)
                spaces_need_to_add -= 1
            else:
                space = " " * full_spaces
            result += space + words[i]

        return result


if __name__ == "__main__":
    s = Solution()
    print(
        s.fullJustify(
            ["This", "is", "an", "example", "of", "text", "justification."], 16
        )
    )
    print(
        s.fullJustify(
            ["What", "must", "be", "acknowledgment", "shall", "be"], 16
        )
    )
    print(
        s.fullJustify(
            [
                "Science",
                "is",
                "what",
                "we",
                "understand",
                "well",
                "enough",
                "to",
                "explain",
                "to",
                "a",
                "computer.",
                "Art",
                "is",
                "everything",
                "else",
                "we",
                "do",
            ],
            20,
        )
    )
    print(
        s.fullJustify(["Listen", "to", "many,", "speak", "to", "a", "few."], 6)
    )

```

<div align='center'><h3><a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/23.Find%20the%20Index%20of%20the%20First%20Occurrence%20in%20a%20String'>⬅️ предыдущая задача</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/README.md'>Все задачи</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/25.Valid%20Palindrome'>следующая задача ➡️</a></h3></div>