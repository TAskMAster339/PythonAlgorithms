# [**16) Trapping Rain Water**](https://leetcode.com/problems/trapping-rain-water/description/)

## **Условие:**

Дан массив из **n** положительных чисел, которые представляют карту высот, где ширина каждого столбика равна **1**. Нужно посчитать сколько воды можно поймать после дождя. (смотри картинку)

## **Идея:**

Вся сложность состоит в том, чтобы вывести формулу для вычисления объема воды в ямке.

## **Реализация:**

Сначала я приведу не очень оптимальное решение, но его последующая оптимизация даст нам искомое решение.

Я буду искать ямки. Под ямкой я понимаю - кортеж (**i**, **j**), такой что **i** < **j**, также выполняется неравенства **height**[**i**] >= **height**[**k**] и **height**[**j**] >= **height**[**k**], для каждого **k**, удовлетворяющему неравенству **i** < **k** < **j**.

Для начала создадим указатель **start** = **0**, который в начале указывает на начло массива. Также создадим множество **result**, в которое мы будем заносить пары (**i**, **j**), где **i** - индекс столбика начала ямы, **j** - индекс столбика окончания ямы, при этом **i** < **j**.

Теперь с помощью цикла **for** **i** **in** **range**(**1**, **len**(**height**)), я буду искать подходящие нам ямки. Условие при котором ямка нам подходит: **height**[**i**] >= **height**[**start**], если мы нашли такую ямку, то мы добавляем её в множество и двигаем указатель **start** на **i** позицию.

Таким образом на этот цикл мы найдем все ямки (**i**, **j**) с начала массива.

Теперь сделаем то же самое, только начнем с конца массива. Мы будем искать те же самые ямки (**i**, **j**). Для этого создадим еще один указатель **end** = **len**(**height**) - **1**. (можно воспользоваться **start**, но для читаемости я не пожадничал и создал еще один указатель). Если **height**[**i**] >= **height**[**end**], то мы нашли ямку, в которой можно поймать воду, записываем её в множество и двигаем **end** на **i** позицию.

После того как мы прошли эти два цикла, мы нашли все возможные ямки, в которых по условию можно поймать какое-то количество воды. (Предлагаю самостоятельно доказать, что два вот таких прохода и два условия **height**[**i**] >= **height**[**start**] и **height**[**i**] >= **height**[**end**] позволяют нам найти все ямки (**i**, **j**))

Ответом будет суммарное количество воды, которое можно поймать в каждой ямке. Чтобы посчитать его пройдемся по всем парам нашего множества. Как будет вычисляться количество воды в ямке? Сначала найдем самый высокий уровень воды, при котором она "не вытекает" из ямки. Это будет минимум из **height**[**i**] и **height**[**j**], потому, что если уровень воды будет выше этого минимума, то эта вода "выльется" из ямки, а нам нужно её поймать. Теперь нам нужно пройти по всем **k**-тым столбикам, находящимся, между **i** и **j** (**i** < **k** < **j**)(**i** и **j** не включаем, так как это границы ямки). Количество воды в этом столбике будет равно минимальной границе минус высота данного столбика. Просуммировав количество воды в столбиках (это интеграл кстати), получим количество воды в ямки.

**water** += **min_height** - **height**[**i**]

Повторяя эту процедуру для каждой ямки, получим суммарное пойманное количество воды в ямках.



После того как задача стала очевидной и простой, можно заняться оптимизированием решения. Например, очевидно, что можно обойтись без множества и последнего цикла для подсчета суммарного количества воды. (Очевидно это, потому что суммарное количество воды в ямках равно сумме количеств воды в ямках, из этой суммы следует линейная независимость нашего алгоритма (Результат сумма, а слагаемые не пересекаются, то есть независимы), а два наших цикла линейны, поэтому мы можем независимо посчитать эти суммы в них) Это можно делать динамически в тех двух циклах, где мы находим ямки (**i**, **j**). Теперь когда мы найдем ямку, то мы добавим в **result** (теперь это просто число), значение воды в этой ямке, которое мы динамически посчитаем.

Рассмотрим первый цикл, а второй будет аналогичным. Создадим вспомогательную переменную **tmp**, в которой будем считать воду в гипотетической ямке, когда наша ямка станет реальной (выполнится необходимое неравенство), ты мы добавим **tmp** в **result**. Для расчета **tmp** нам понадобится минимальная высота **small** в этой ямке, она будет равна **height**[**start**], так как реальная ямка, найденная в нашем цикле должна удовлетворять условию: **height**[**i**] >= **height**[**start**], то очевидно, что **small** = **height**[**start**].

Теперь по формуле выведенной в первом решении, получим что **tmp** += **small** - **height**[**i**], только нужно учесть, что мы добавляем эту разность в **tmp**, только если она >=**0**, иначе мы просто добавляем **0**.

Когда мы найдем подходящую нам ямку, мы просто добавляем в **result** += **tmp**, двигаем указатель **start** на **i** позицию и не забываем обнулить **tmp**.

Для второго цикла аналогично, только стоит не забыть про две вещи: **1**) обязательно обнулить **tmp** после первого цикла(либо создать новую временную переменную, проинициализировав её **0**), **2**) условие ямки должно быть **height**[**i**] > **height**[**end**], так как мы отказались от множества, то мы теперь можем столкнуться с пересчетом уже посчитанных ямок, чтобы этого избежать мы делаем это неравенство строгим.



## **Оценка:**

Первый алгоритм затратит **O**(**N**) времени. По памяти оценить его сложно так как мы сохраняем пары (**i**, **j**), но в теории в наихудшим случае у нас будет **N** * (**N** - **1**) / **2** пар, сохранено в множестве, что говорит об затратах по памяти **O**(**N**^**2**), но вероятность наихудшего исхода при **N** стремящимся к бесконечности стремится к **0**, поэтому в среднем будет затрачено **O**(**1**) памяти. Второе решение затратит **O**(**N**) времени, при этом константа будет намного меньше, следовательно алгоритм будет быстрее(скорость увеличится примерно в **1**.**5** раза). В этом случае память уже точно будет **O**(**1**).

## Код:
```python
from typing import List


class Solution:
    def merge(
        self, nums1: List[int], m: int, nums2: List[int], n: int
    ) -> None:
        m, n, i = m - 1, n - 1, m + n - 1
        while n >= 0:
            if m >= 0 and nums1[m] > nums2[n]:
                nums1[i] = nums1[m]
                m -= 1
            else:
                nums1[i] = nums2[n]
                n -= 1
            i -= 1


if __name__ == "__main__":
    s = Solution()
    s.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
    s.merge([1], 1, [], 0)
    s.merge([0], 0, [1], 1)
    s.merge([1, 0], 1, [2], 1)

```

## Код:
```python
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1
        return index

```

## Код:
```python
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
        return j

```

## Код:
```python
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 1
        w = 0
        flag = True
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                count += 1
            else:
                count = 1
            if count > 2 and flag:
                w = i + 1
                flag = False
            if w != 0 and count <= 2:
                nums[w] = nums[i + 1]
                w += 1
        if w == 0:
            return len(nums)
        return w

    def removeDuplicates2(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)

        slow = 2

        for fast in range(2, len(nums)):
            if nums[fast] != nums[slow - 2]:
                nums[slow] = nums[fast]
                slow += 1

        return slow


if __name__ == "__main__":
    s = Solution()
    print(s.removeDuplicates([1, 1, 1, 2, 2, 3]))
    print(s.removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3]))

```

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

## Код:
```python
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        target = 0
        zero_flag = False
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] == 0 and not zero_flag:
                target = 2
                zero_flag = True
            elif target != 0:
                if nums[i] >= target:
                    target = 0
                    zero_flag = False
                else:
                    target += 1
        return target == 0


if __name__ == "__main__":
    s = Solution()
    print(s.canJump([2, 3, 1, 1, 4]))
    print(s.canJump([3, 2, 1, 0, 4]))
    print(s.canJump([0, 2, 3]))
    print(s.canJump([2, 0, 1, 0, 1]))
    print(s.canJump([3, 0, 0, 0]))
    print(s.canJump([1, 0, 0, 1, 1, 2, 2, 0, 2, 2]))

```

## Код:
```python
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        near = far = jumps = 0

        while far < len(nums) - 1:
            farthest = 0
            for i in range(near, far + 1):
                farthest = max(farthest, i + nums[i])

            near = far + 1
            far = farthest
            jumps += 1

        return jumps

    def jump2(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0  # Already at the last index

        jumps = 0
        current_end = 0
        farthest = 0

        for i in range(n - 1):  # No need to check the last element
            # Update the farthest point reachable from here
            jump = i + nums[i]
            if farthest < jump:
                farthest = jump

            # If we have reached the end of the current jump's range
            if i == current_end:
                jumps += 1
                current_end = farthest

                # If the current_end reaches or goes beyond the last index
                if current_end > n - 1:
                    break

        return jumps


if __name__ == "__main__":
    s = Solution()
    print(s.jump2([2, 3, 1, 1, 4]))
    print(s.jump2([2, 3, 0, 1, 4]))
    print(s.jump([1, 2]))
    print(s.jump([1, 2, 3]))
    print(s.jump([0]))
    print(s.jump([1, 2, 1, 1, 1]))  # 3

```

## Код:
```python
from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        papers = len(citations)
        h_indexes = [0] * (papers + 1)

        for citation in citations:
            h_indexes[min(citation, papers)] += 1

        states = 0
        for h in range(papers, -1, -1):
            states += h_indexes[h]
            if states >= h:
                return h


# [] - 0
# [2] - 1 / [0] = 0
# [2, 17] = 2 - prev if current >= prev_h and current >= max_h else prev + 1
# [1, 29, 10] = 2
# [1, 29, 10, 2] = 2

# [0] = 0
# [0, 1, 2] =

# [1] = 1
# [1, 3] = 1
# [1, 3, 2] = 2

if __name__ == "__main__":
    s = Solution()
    print(s.hIndex([3, 0, 6, 1, 5]))
    print(s.hIndex([1, 3, 1]))
    print(s.hIndex([0, 1]))
    print(s.hIndex([11, 15]))

```

## Код:
```python
import random


class RandomizedSet:
    def __init__(self):
        self.lst = []
        self.idx_map = {}

    def search(self, val):
        return val in self.idx_map

    def insert(self, val):
        if self.search(val):
            return False

        self.lst.append(val)
        self.idx_map[val] = len(self.lst) - 1
        return True

    def remove(self, val):
        if not self.search(val):
            return False

        idx = self.idx_map[val]
        self.lst[idx] = self.lst[-1]
        self.idx_map[self.lst[-1]] = idx
        self.lst.pop()
        del self.idx_map[val]
        return True

    def getRandom(self):
        return random.choice(self.lst)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()


if __name__ == "__main__":
    obj = RandomizedSet()
    param_1 = obj.insert(2)
    param_2 = obj.insert(3)

    param_4 = obj.getRandom()
    print(param_1, param_2, param_4)

```

## Код:
```python
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums)
        prefix[0] = nums[0]
        suffix = [0] * len(nums)
        suffix[-1] = nums[-1]

        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i]

        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i]

        result = [0] * len(nums)
        for i in range(len(nums)):
            if i + 1 == len(nums):
                result[i] = prefix[i - 1]
            elif i == 0:
                result[i] = suffix[i + 1]
            else:
                result[i] = suffix[i + 1] * prefix[i - 1]
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.productExceptSelf([1, 2, 3, 4]))
    print(s.productExceptSelf([-1, 1, 0, -3, 3]))

```

## Код:
```python
from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_fuel = 0
        for i in range(len(gas)):
            total_fuel += gas[i] - cost[i]

        if total_fuel < 0:
            return -1

        fuel = 0
        result = 0
        for i in range(len(gas)):
            fuel += gas[i] - cost[i]
            if fuel < 0:
                fuel = 0
                result = i + 1

        return result

        # fuel = 0
        # count = 0
        # result = 0
        # for i in range(len(gas) * 2):
        #     fuel += gas[i % len(gas)] - cost[i % len(gas)]
        #     if count == len(gas):
        #         return result
        #     if fuel < 0:
        #         fuel = 0
        #         result = (i + 1) % len(gas)
        #         count = 0
        #         continue
        #     count += 1
        # return -1


if __name__ == "__main__":
    s = Solution()
    print(s.canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))
    print(s.canCompleteCircuit([1, 2, 3, 4, 2, 12], [3, 4, 5, 1, 6, 1]))
    print(s.canCompleteCircuit([2, 3, 4], [3, 4, 3]))

```

## Код:
```python
from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [1] * len(ratings)

        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)
        print(candies)
        return sum(candies)


if __name__ == "__main__":
    s = Solution()
    print(s.candy([1, 0, 2]))
    print(s.candy([1, 3, 4, 5, 2]))
    print(s.candy([1, 3, 2, 2, 1]))

```

## Код:
```python
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        start = 0
        result = set()
        for i in range(1, len(height)):
            if height[i] >= height[start]:
                result.add((start, i))
                start = i
        end = len(height) - 1
        for i in range(len(height) - 2, -1, -1):
            if height[i] >= height[end]:
                result.add((i, end))
                end = i
        water = 0
        for pair in result:
            min_height = min(height[pair[0]], height[pair[1]])
            for i in range(pair[0] + 1, pair[1]):
                water += min_height - height[i]
        return water

    def trap2(self, height: List[int]) -> int:
        start = 0
        result = 0
        tmp = 0
        for i in range(1, len(height)):
            small = height[start]
            tmp += (small - height[i]) if (small - height[i]) > 0 else 0
            if height[i] >= height[start]:
                result += tmp
                start = i
                tmp = 0
        end = len(height) - 1
        tmp = 0
        for i in range(len(height) - 2, -1, -1):
            small = height[end]
            tmp += (small - height[i]) if (small - height[i]) > 0 else 0
            if height[i] > height[end]:
                result += tmp
                end = i
                tmp = 0
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))  # 6
    print(s.trap([4, 2, 0, 3, 2, 5]))  # 9

```

