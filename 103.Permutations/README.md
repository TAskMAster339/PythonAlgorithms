<div align='center'>
<h1><a href='https://leetcode.com/problems/permutations/description/'><strong>103) Permutations</strong></a></h1>
</div>

## **Условие:**

Дан массив **nums** с уникальными числами. Необходимо вернуть все возможные перестановки этих чисел. Ответ может быть в любом порядке

## **Идея:**

Вспомнить что такое перестановки

## **Реализация:**

Идем по тому же сценарию: создаем рекурсивную функцию **backtrack**, с помощью которой будем вычислять наши перестановки.

Крайний случай - глубина рекурсии стала равна длине **nums**, то есть мы переставили каждый элемент. Тогда записываем копию массива **nums** в массив **result** и возвращаемся.

Рекуррентный случай - в цикле проходим по всем индексам от **start** (глубины рекурсии) до **len**(**nums**). Мы будем менять местами **nums**[**start**] и **nums**[**i**]. После этого вызвать **backtrack**(**start** + **1**), после возврата меняем всё обратно.

Таким образом каждая каждый вызов **backtrack** будет менять элемент **nums**[**start**] со всеми элементами списка, индекс которых больше или равен **start**. Такими перестановками мы получим все возможные перестановки.



## **Оценка:**

Верхняя оценка по памяти получается **O**(**N** * **N**!), где **N** - длина массива **nums** (количество чисел для перестановки). Она получается так: всего существует **N**! перестановок, но каждую мы будем записывать в массив **result**, что затратим **O**(**N**) на копирование. Отсюда итоговая сложность **O**(**N** * **N**!)

Верхняя оценка по памяти будет **O**(**N**), так как **N** - длина любой перестановки. Поэтому стек вызовов в наихудшем случае будет занят **O**(**N**) элементами.

## Код:
```python
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []

        def backtrack(start):
            if start == len(nums):
                result.append(nums[:])
                return

            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]

        backtrack(0)
        return result


if __name__ == "__main__":
    f = Solution().permute
    print(f([1, 2, 3]))
    print(f([0, 1]))
    print(f([1]))

```

<div align='center'><h3><a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/102.Combinations'>⬅️ предыдущая задача</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/README.md'>Все задачи</a></h3></div>