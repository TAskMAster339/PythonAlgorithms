<div align='center'>
<h1><a href='https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/description/'><strong>148) Best Time to Buy and Sell Stock III</strong></a></h1>
</div>

## **Условие:**

Дан массив цен **prices**, где **prices**[**i**] это стоимость акции на **i**-тый день.

Необходимо найти максимально возможный профит, которые можно получить покупая и продавая акции максимум **2** раза.

Надо учесть, что можно покупать акцию второй раз только после того, как первая купленная была продана

## **Идея:**

Просто симулировать ситуацию на бирже

## **Реализация:**

Нам понадобиться найти **4** числа, которые представляют собой **2** промежутка, один из которых раньше второго.

Будем искать вот так: создадим следующие переменные: **buy1** и **buy2** - это минимальная цена акции при первой и второй покупки соответственно. **profit1** и **profit2** - выгода, полученная при продажи первой и второй акции.

Осталось просто пройтись по всем ценам, пытаясь совершить первую покупку за минимальную цену и продать за максимальную. Затем повторяем, учитывая, что мы уже получили какую-то прибыль.

План такой:

**1**) **buy1** = **min**(**buy1**, **price**) - определяем наименьшую стоимость акции для покупки.

**2**) **profit1** = **max**(**profit1**, **price** - **buy1**) - делаем профит после первой покупки максимальным.

**3**) **buy2** = **min**(**buy2**, **price** - **profit1**) - то же, что и **buy1**, только учитываем что у нас уже есть профит **profit1**, который покроет некоторые расходы.

**4**) **profit2** = **max**(**profit2**, **price** - **buy2**) - получаем профит после второй покупки, он уже включает в себя **profit1**.



## **Оценка:**

Сложность по времени будет **O**(**N**), где **N** - это **len**(**prices**).

Сложность по памяти будет **O**(**1**).

## Код:
```python
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy1 = buy2 = float("inf")
        profit1 = profit2 = 0

        for price in prices:
            buy1 = min(buy1, price)
            profit1 = max(profit1, price - buy1)

            buy2 = min(buy2, price - profit1)
            profit2 = max(profit2, price - buy2)

        return profit2


if __name__ == "__main__":
    f = Solution().maxProfit
    print(f([3, 3, 5, 0, 0, 3, 1, 4]))  # 6
    print(f([1, 2, 3, 4, 5]))  # 4
    print(f([7, 6, 4, 3, 1]))  # 0

```

<div align='center'><h3><a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/147.Edit%20Distance'>⬅️ предыдущая задача</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/README.md'>Все задачи</a></h3></div>