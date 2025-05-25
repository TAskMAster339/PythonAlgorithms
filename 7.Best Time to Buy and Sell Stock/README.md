<div align='center'>
<h1><a href='https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/'><strong>7) Best Time to Buy and Sell Stock</strong></a></h1>
</div>

Идея: ищем динамически минимум, параллельно сравнивая его с "максимумом"

Нам нужно две переменные, одна для хранения результата, её мы вернем. Другая для динамического подсчета миниума, так как числа у нас меньше **10**^**4**, присвоим минмуму **10**^**4** + **1**.

Далее идем по массиву, динамически вычисляя минимум. Затем, после того как мы сравнили **i**-ый элемент с минимумом, мы сравниваем разность этого же элемента и минимума с результатом. Если данная разность (наша прибыль) больше чем результат, то мы обновляем наш результат.

Таким образом, всего за один проход по списку, мы зафиксируем нашу прибыль.

**Stonks** всего за **O**(**n**) секунд.

## Код:
```python
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        min = 10001
        for i in range(0, len(prices)):
            if prices[i] < min:
                min = prices[i]
            if result < prices[i] - min:
                result = prices[i] - min
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.maxProfit([7, 1, 5, 3, 6, 4]))
    print(s.maxProfit([7, 6, 4, 3, 1]))
    print(s.maxProfit([1, 2]))

```

<div align='center'><h3><a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/6.Rotate%20Array'>⬅️ предыдущая задача</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/README.md'>Все задачи</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/8.Best%20Time%20to%20Buy%20and%20Sell%20Stock%20II'>следующая задача ➡️</a></h3></div>