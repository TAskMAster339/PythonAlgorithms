# [**7) Best Time to Buy and Sell Stock**](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/)

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

