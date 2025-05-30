<div align='center'>
<h1><a href='https://leetcode.com/problems/rotate-array/description/'><strong>6) Rotate Array</strong></a></h1>
</div>

Идея: использовать инверсию.

Наша задача сделать циклический сдивг массива. Для этого сначала разделим размер сдвига **k** на длину списка **len**(**nums**) по модулю. Сильная экономия так как результат сдвига массива с **10** элементами или на **1**, или на **11**, или на **21** и т. д будет одинаковым.

Самое эффективное и простое решение - сделать три инверсии массива. Во-первых, мы инвертируем весь массив. Во-вторых, инвертируем элементы с начала массива до **k**. В-третьих, инвертируем элементы с **k** до конца. Вуаля, решение готово. Осталось только реализовать функцию инверсии. Функция **invert** будет принимать массив, индекс старта диапазона инверсии, индекс конца диапазона. В самой фукции мы будем менять пары элементов: первый с последним, второй с предпоследним и т. д.

Первая инверсия пройдет половину массива и потребует **O**(**n**/**2**) времени, вторая **O**(**k**/**2**), третья **O**((**n**-**k**)/**2**). После отбрасывания коэффицентов и констант, поучим **O**(**n**) + **O**(**1**) + **O**(**n**) = **2O**(**n**) = **O**(**n**).

Время алгоритма - линейное **O**(**n**).

## Код:
```python
from typing import List


def invert(nums, start, end):
    for i in range(start, (start + end) // 2):
        nums[i], nums[end - 1] = nums[end - 1], nums[i]
        end -= 1


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k %= len(nums)
        invert(nums, 0, len(nums))
        invert(nums, 0, k)
        invert(nums, k, len(nums))


if __name__ == "__main__":
    s = Solution()
    s.rotate([1, 2, 3, 4, 5, 6, 7], 3)
    s.rotate([-1, -100, 3, 99], 2)

```

<div align='center'><h3><a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/5.Majority%20Element'>⬅️ предыдущая задача</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/README.md'>Все задачи</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/7.Best%20Time%20to%20Buy%20and%20Sell%20Stock'>следующая задача ➡️</a></h3></div>