<div align='center'>
<h1><a href='https://leetcode.com/problems/coin-change/description/'><strong>140) Coin Change</strong></a></h1>
</div>

## **Условие:**

Вам дан массив целых чисел **coins**, которые представляет собой номиналы монет, и число **amount**, которое представляет сумму денег, которую нужно собрать из монет.

Необходимо посчитать наименьшее число монет, которых хватит, чтобы собрать сумму **amount**. Если из номиналов **coins** нельзя собрать сумму, то необходимо вернуть -**1**

## **Идея:**

Можно заметить, что номиналы монеток представляют собой виды ходов, **amount** - расстояние, которое надо пройти этими ходами. Тогда задача сводиться к определению наименьшего количества ходов, за которое можно пройти расстояние **amount**

## **Реализация:**

Создадим массив **dp**, который заполним бесконечностями (Так как мы будем искать минимальный путь). **dp**[**i**] - минимальное количество монет необходимое, чтобы собрать сумму **i**. Искомый ответ будет лежать в **dp**[**amount**].

Крайний случай это **i** = **0**, **dp**[**0**] = **0**. Далее динамически будем для каждого **i**-того значения перебирать все имеющиеся у нас номиналы монеток, если **i** >= **coin**, значит в теории как-то возможно собрать сумму **amount**, поэтому пересчитываем **dp**[**i**] как минимум из **dp**[**i**] и **dp**[**i** - **coin**] + **1** (Количество монет, необходимое для суммы **i** - **coin** плюс **1** монета).



## **Оценка:**

По времени алгоритм займет **O**(**N** * **amount**), где **N** - длина массива **coins**.

По памяти будет **O**(**amount**), расходы на память в массиве.

## Код:
```python
class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[amount] if dp[amount] != float("inf") else -1


if __name__ == "__main__":
    f = Solution().coinChange
    print(f([1, 2, 5], 11))  # 3
    print(f([2], 3))  # -1
    print(f([1], 0))  # 0
    print(f([186, 419, 83, 408], 6249))  # 20

```

<div align='center'><h3><a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/139.Word%20Break'>⬅️ предыдущая задача</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/README.md'>Все задачи</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/141.Longest%20Increasing%20Subsequence'>следующая задача ➡️</a></h3></div>