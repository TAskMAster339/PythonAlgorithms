<div align='center'>
<h1><a href='https://leetcode.com/problems/maximum-subarray/description/'><strong>112) Maximum Subarray</strong></a></h1>
</div>

## **Условие:**

Дан массив целых чисел **nums**, необходимо найти подмассив с наибольшей суммой и вернуть эту сумму.

Подмассив - непрерывная последовательность элементов массива

## **Идея:**

Воспользоваться алгоритмом Кадане

## **Реализация:**

Идея алгоритма Кадане состоит в том, что мы циклом пройдем по всему массиву. Каждую итерацию мы будем считать сумму подмассива.

Для этого будем создавать подмассив, тогда необходимо решить поможет ли **i**-тое число увеличить сумму подмассива. Если оно увеличивает сумму, то мы увеличиваем сумму на это число. А если **i**-тое число оказалось больше суммы предыдущего массива + само это число, то нам выгоднее начать новый подмассив с новой суммой, которая в начале будет равняться **i**-тому числу.

При этом каждую итерацию запоминаем самую наибольшую вычисленную сумму. В конце она и будет искомым ответом.



## **Оценка:**

Сложность по времени алгоритма Кадане будет **O**(**N**), где **N** - количество элементов в массиве. Сложность по памяти алгоритма Кадане будет **O**(**1**), так как не используется какая-либо дополнительная память.

## Код:
```python
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        summary = 0
        result = nums[0]
        for num in nums:
            summary = max(num, summary + num)
            result = max(result, summary)

        return result


if __name__ == "__main__":
    f = Solution().maxSubArray
    print(f([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
    print(f([1]))  # 1
    print(f([5, 4, -1, 7, 8]))  # 23

```

<div align='center'><h3><a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/111.Merge%20k%20Sorted%20Lists'>⬅️ предыдущая задача</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/README.md'>Все задачи</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/113.Maximum%20Sum%20Circular%20Subarray'>следующая задача ➡️</a></h3></div>