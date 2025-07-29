<div align='center'>
<h1><a href='https://leetcode.com/problems/maximum-sum-circular-subarray/description/'><strong>113) Maximum Sum Circular Subarray</strong></a></h1>
</div>

## **Условие:**

Дан цикличный массив целых чисел **nums** длины **n**, нужно вернуть максимально возможную сумму непустого подмассива **nums**.

Циклический массив означает, что перед **0** элементом идет последний. После последнего идет **0** элемент.

В подмассиве каждый элемент может встречаться только один раз

## **Идея:**

Нужно допилить алгоритм Кадане для этого циклического массива

## **Реализация:**

Подмассив с максимальной суммой может быть расположен либо в центре массива, то есть без зацикливания, либо с краю массива, тогда у нас по факту он будет разделен на два массива, один будет у левого края массива, другой будет у правого края массива.

Очень интересно теперь подумать, что за подмассив в этом случае располагается по середине массива. Очевидно, что по центру будет расположен подмассив с минимальной суммой. (Это так, потому что только в этом случае, наши крайние массивы будут обладать наибольшей суммой).

Тогда применим алгоритм Кадане для поиска двух подмассивов в исходном. Первый подмассив будет иметь максимальную сумму, второй минимальную сумму.

В конце необходимо вернуть максимум из суммы максимального подмассива и разности суммы массива и суммы минимального подмассива (**sum_max** = **sum_total** - **sum_min**)

Еще стоит не забыть про очень неприятный случай, когда все числа в массиве отрицательные, в этом случае нужно просто вернуть максимальную сумму подмассива. (**sum_total** - **sum_min**, если **sum_min** == **sum_total** окажется равным **0**, что помешает корректно посчитать максимум).



## **Оценка:**

Сложность по времени будет **O**(**N**), где **N** - количество элементов в массиве.

Сложность по памяти будет **O**(**1**), так как мы создаем всего лишь **5** переменных.

## Код:
```python
class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        max_sum = min_sum = cur_max = cur_min = total_sum = nums[0]
        for i in range(1, len(nums)):
            cur_max = max(nums[i], cur_max + nums[i])
            max_sum = max(max_sum, cur_max)

            cur_min = min(nums[i], cur_min + nums[i])
            min_sum = min(min_sum, cur_min)

            total_sum += nums[i]

        if min_sum == total_sum:
            return max_sum
        return max(max_sum, total_sum - min_sum)


if __name__ == "__main__":
    f = Solution().maxSubarraySumCircular
    print(f([1, -2, 3, -2]))  # 3
    print(f([5, -3, 5]))  # 10
    print(f([-3, -2, -3]))  # -2

```

<div align='center'><h3><a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/112.Maximum%20Subarray'>⬅️ предыдущая задача</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/README.md'>Все задачи</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/114.Search%20Insert%20Position'>следующая задача ➡️</a></h3></div>