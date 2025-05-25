<div align='center'>
<h1><a href='https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/'><strong>8) Best Time to Buy and Sell Stock II</strong></a></h1>
</div>

Идея: нужно как-то динамически это посчитать

Для начала докажим следующую лемму: максимальный стонкс в диапозоне будет равен сумме положительных разностей следующего элемента с текущим. Например, [**1**, **2**, **3**, **4**, **5**]. стонкс будет равен **5** - **1** = **4**. Но если мы воспользуемся нашей леммой, то получим:

**2** - **1** = **1**

**3** - **2** = **1**

**4** - **3** = **1**

**5** - **4** = **1**

= **4**, мы получили тот же самый результат. Это будет работать для любого стонкса, так как каждый стонкс можно представить в виде суммы подстонксов. (Мы представили в виде суммы пар)

Получаем следующие простое решение. Создаем переменную **result**, которую вернем. Идем по списку циклом **for** до **len**(**prices**) - **1**, так как сравниваем пары. Если **prices**[**i**] < **prices**[**i**+**1**] (следовательно сумма положительна), то мы добавляем эту разность в **result**.

Так мы сделали всего дин проход по списку, время выполнинея будет **O**(**n**).

## Код:
```python
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        for i in range(len(prices) - 1):
            if prices[i] < prices[i + 1]:
                result += prices[i + 1] - prices[i]
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.maxProfit([7, 1, 5, 3, 6, 4]))
    print(s.maxProfit([1, 2, 3, 4, 5]))
    print(s.maxProfit([7, 6, 4, 3, 1]))

```

<div align='center'><h3><a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/7.Best%20Time%20to%20Buy%20and%20Sell%20Stock'>⬅️ предыдущая задача</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/README.md'>Все задачи</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/9.Jump%20Game'>следующая задача ➡️</a></h3></div>