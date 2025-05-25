<div align='center'>
<h1><a href='https://leetcode.com/problems/majority-element/description/'><strong>5) Majority Element</strong></a></h1>
</div>

Идея: ищем моду, в условии дана огромная подсказка как это сделать за один пробег.

Решение следующие. Во-первых, мы, прочитав условие, понимаем, что самый частый элемент в массиве (мода) встречается более **n** / **2** раз, где **n** - длина массива. Во-вторых, мы делаем вывод, что если мы создадим счетчик, который будет инкрементироваться каждый раз, когда мы встречаем моду и декрементироваться каждый раз при встрече другого числа. То такой счетчик всегда будет больше **0**. (Подумайте об этом, это очень важно)

Итак, мы создадим переменную **result**, в которую запишем искомую моду, и счетчик **count**. После этого пройдем по массиву циклом **for**-**each**. Кажую итерацию мы будем сравнивать **i** == **result**, если они равны, то мы делаем **count** += **1**, иначе **count** -= **1**. Далее важный момент - **count** == **0**, это значит, что мы нашли вторую "моду" (на данный момент цикла она будет такой же модой, как и перая), значит в **result** нужно присвоить новонайденную моду(не факт, что она правильная). Таким образом у нас будет постоянная происходить гонка мод, но благодаря условию, что самый частый элемент встречается более чем **n** / **2** раз, мы можем быть спокойны и уверены, что в коцне концов настоящая мода победит и будет записанна в **result**.

Сложность алгоритма - **O**(**n**), где **n** - длина массива.

## Код:
```python
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        result = 0
        count = 0

        for i in nums:
            if count == 0:
                result = i

            count += 1 if i == result else -1

        return result


if __name__ == "__main__":
    s = Solution()
    print(s.majorityElement([3, 2, 3]))
    print(s.majorityElement([2, 2, 1, 1, 1, 2, 2]))

```

<div align='center'><h3><a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/4.Remove%20Duplicates%20from%20Sorted%20Array%20II'>⬅️ предыдущая задача</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/README.md'>Все задачи</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/6.Rotate%20Array'>следующая задача ➡️</a></h3></div>