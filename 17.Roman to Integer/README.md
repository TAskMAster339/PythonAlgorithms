<div align='center'>
<h1><a href='https://leetcode.com/problems/roman-to-integer/description/'><strong>17) Roman to Integer</strong></a></h1>
</div>

## **Условие:**

Дано римское число, нужно перевести его в нормальное.

## **Идея:**

Хэш-таблица.

## **Реализация:**

Создадим словарь **table**, где ключами будут римские цифры, а значениями их значение в арабских цифрах. ("**I**": **1**, "**V**": **5** и так далее) Создадим переменную **prev**, в которой будем хранить предыдущую римскую цифру, это нужно для случаев **IV**, **IX** и подобных. В этих случаях нам нужно из большей цифры вычесть меньшую. Инициализируем **prev** первой римской цифрой. Создаем переменную **result**, которую инициализируем **table**[**prev**], арабское значение римской цифры.

Далее проходим циклом по римским цифрам, динамически высчитывая **result**. Нужно учесть ранее упомянутый случай, когда **table**[**s**[**i**]] > **table**[**prev**], в этом случае мы из **result** вычитаем **table**[**prev**] (так как оно зря было добавлено в **result**, на предыдущей итерации) и добавляем **table**[**s**[**i**]] - **table**[**prev**]. Если римская цифра меньше или равна предыдущей, то мы просто прибавляем её значение в **result**. Также не забываем обновлять значение **prev** в конце каждой итерации.

После окончания цикла в переменной **result** будет записано искомое число, его мы и возвращаем.



## **Оценка:**

По времени мы потратим **O**(**N**), по памяти **O**(**1**), так как у нас существует ограниченное количество римских цифр (**7** всего), поэтому её размер будет константным, или можно показать, что её размер никак не зависит от **N**, в обоих случаях получаем постоянную память. На самом деле можно еще лучше оптимизировать алгоритм, заменив хэш-таблицу двумя массивами, у которых по соответствующим индексам будут находится римская цифра и её значение. (["**I**", "**V**", ...] [**1**, **5**, ...]). Тем самым мы получим ту же самую хэш-таблицу, только данная реализация гарантирует в наихудшем случае доступ к элементам **O**(**1**), что оптимизирует время, а отсутствие накладных расходов на реализацию хэш-таблицы(Разрешение коллизии, ...) мы сэкономим память.

## Код:
```python
class Solution:
    def romanToInt(self, s: str) -> int:
        table = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        prev = s[0]
        result = table[s[0]]
        for i in range(1, len(s)):
            if table[s[i]] > table[prev]:
                #    result -= table[prev]
                result += table[s[i]] - 2 * table[prev]
            else:
                result += table[s[i]]
            prev = s[i]
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.romanToInt("III"))
    print(s.romanToInt("LVIII"))
    print(s.romanToInt("MCMXCIV"))

```

<div align='center'><h3><a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/16.Trapping%20Rain%20Water'>⬅️ предыдущая задача</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/README.md'>Все задачи</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/18.Integer%20to%20Roman'>следующая задача ➡️</a></h3></div>