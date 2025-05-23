# [**10) Jump Game II**](https://leetcode.com/problems/jump-game-ii/description/)

Идея: очевидно, что нужно как-то динамически рассчитывать самый дальний прыжок из клетки, где мы стоим.

Для этого создадим три ключевые переменные - **near**, **far**, **jumps**, **near** - индекс ближайшего прыжка, **far** - индекс самого выгодного прыжка. (Самый выгодный прыжок тот, после которого мы либо дойдем до конца, либо сможем сделать еще один самый выгодный прыжок). Ну а **jumps** будет общим счетчиком наших прыжков, его мы вернем в конце процедуры.

Создадим два цикла, первый будет итерироваться до тех пор, пока индекс самого выгодного прыжка меньше, чем длина входного массива минус один. Второй цикл нужен для вычисления следующего индекса самого выгодного прыжка. Затем мы просто обновляем наши переменные: **near** становиться следующим за **far** индексом, **far** становиться индексом самого выгодного прыжка, **jumps** инкрементируется.

В итоге мы получим один вложенный цикл, но это не особая проблема, так как он всегда будет много меньше по сравнению с **N**, и поскольку в нем вообще не фигурирует **N**, то его можно считать за константу, правда эта константа очень большая. Поэтому эффективность данного алгоритма **O**(**N**).

Однако, поискав я нашел, как развернуть этот цикл. Теперь мы создаем переменные для подсчета прыжков, индекса конца (Туда куда мы можем максимум допрыгнуть) и переменную, хранящую наш самый длинный прыжок. Идея следующая, мы идем по массиву, узнаем на сколько мы можем прыгнуть, и вычисляем самый длинный прыжок. Индекс конца будет равен нашему индексу плюс наш самый длинный прыжок. Теперь нам остается повторять этот алгоритм, либо до конца цикла, либо до того как наш конец превысит длину массива.

Для лучшего понимания этот алгоритм можно интерпретировать вот так. У нас есть две задачи. **1**) Идти по массиву с **0** до конца. **2**) Искать самый длинный прыжок из прыжков, которые мы встретим на пути. В начале наш самый длинный прыжок, тот с которого мы начали. Например, он равен **3**. Далее мы идем на три клетки вперед, параллельно смотря ну содержащиеся в этих клетках прыжки, таким образом мы находим наибольший прыжок в этом промежутке. После того как мы дошли до **3** клетки. Мы увеличиваем счетчик количества прыжков на один, затем продолжаем наш алгоритм аналогичным образом, только теперь в начале нашим самым длинным прыжком будет максимум из значения клетки, на которой мы остановились, и найденного ранее самого длинного прыжка.

Таким образом, за один проход, мы гарантировано посчитаем минимальное количество прыжков, которое нужно, чтобы добраться с начала до конца массива. Эффективность **O**(**N**), но тут уже константа менее значима, это хорошо заметно при маленьких тестах. При больших тестах время решений будет отличаться только в пределах погрешности.

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

