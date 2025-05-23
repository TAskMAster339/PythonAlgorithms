# [**24) Text Justification**](https://leetcode.com/problems/text-justification/description/)

## **Условие:**

Дан массив строк **words** и ширина **maxWidth**, нужно отформатировать текст таким образом, чтобы каждая строка в нем была длиной в **maxWidth** символов и была выравнена по ширине. В строке должно быть так много слов, насколько возможно. Слова разделяются пробелами. Пробелы в строке распределяются равномерно, если это невозможно, то слева на право. Последняя строка текста должна быть выровнена по левому краю.

## **Идея:**

Нужно реализовать две вещи: **1**) деление слов по строкам, **2**) расстановка пробелов.

## **Реализация:**

**1**) Создадим массив **result**, в который будем записывать строки, состоящий из слов, разделенных одним пробелом. С помощью цикла, пробегающего по всем словам, мы будем пытаться составить самую длинную строку, меньшую чем **maxWidth**, когда добавить еще одно слово в эту строку невозможно, то мы добавляем её в массив **result**. После цикла нужно проверить то, что осталось во временной строке **tmp_string**. Если она не пустая, то добавляем её в конец массива, это будет наша последняя строка.

**2**) Теперь пробегаемся по всем строкам нашего массива **result**, производя выравнивание по ширине. С помощью функции **justify**(**line**, **width**) я выравниваю строку по ширине. Для этого я рассчитываю **2** основных числа, первое число - это количество равномерно распределенных пробелов, второе число - это пробелы, которые надо распределить неравномерно. Например, если у нас есть **2** слова размером по **6** и **7** букв, а **maxWidth**==**16**, то количество пробелов должно быть **16** - **6** - **7** = **3**. Равномерное количество будет равно **1**, также есть один неравномерный пробел, который будет идти после **1** слова (по условию задачи).

Мы преобразуем нашу строку в массив слов, после чего в цикле конкатенируем эти слова с пробелами, учитывая ранее посчитанное количество равномерных и неравномерных пробелов. В конце функция возвращает строку, выравненную по ширине.

Остается особо обработать последнюю строку. В ней все слова разделены одним пробелом и в конце просто дописываем столько пробелов, сколько необходимо для того, чтобы длина строки равнялась **maxWidth**.

В итоге в **result** записан искомый ответ.

## **Оценка:**

По времени мы потратим **O**(**N** * **K**), где **N** - количество слов, **K** - количество слов в одной строке. По условиям задачи **K** будет очень мало, так как оно зависит от **maxWidth** (**maxWidth** ограничено в диапазоне от **1** до **100**), при **maxWidth**, стремящемся к бесконечности, время будет стремится к **O**(**N**^**2**), в нашем случае будет **O**(**N**). По памяти мы будем хранить массив строк, это **O**(**N**), также процедура **justify**, потребует **O**(**N**). Суммарно получим **O**(**N**) затрат по памяти.

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

## Код:
```python
class Solution:
    def romanToInt(self, s: str) -> int:
        table = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        prev = s[0]
        result = table[s[0]]
        for i in range(1, len(s)):
            if table[s[i]] > table[prev]:
                #    result -= table[prev]
                result += table[s[i]] - 2 * table[prev]
            else:
                result += table[s[i]]
            prev = s[i]
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.romanToInt("III"))
    print(s.romanToInt("LVIII"))
    print(s.romanToInt("MCMXCIV"))

```

## Код:
```python
class Solution:
    def intToRoman(self, num: int) -> str:
        table = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I",
        }
        result = ""
        for i in table.keys():
            while num >= i:
                num -= i
                result += table[i]
            # n = num // i
            # num %= i
            # result += (table[i] * n)

        return result


if __name__ == "__main__":
    s = Solution()
    print(s.intToRoman(3749))
    print(s.intToRoman(58))
    print(s.intToRoman(1994))

```

## Код:
```python
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        for i in range(len(s) - 1, -1, -1):
            if count == 0 and s[i] == " ":
                continue
            if s[i] != " ":
                count += 1
            else:
                break
        return count


if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLastWord("Hello World"))
    print(s.lengthOfLastWord("   fly me   to   the moon  "))
    print(s.lengthOfLastWord("luffy is still joyboy"))

```

## Код:
```python
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = "0" * 201

        for i in strs:
            if len(i) < len(prefix):
                prefix = i

        for word in range(len(strs)):
            word = strs[word]
            for i in range(min(len(word), len(prefix))):
                if word[i] != prefix[i]:
                    prefix = prefix[:i]
                    break
        return prefix


if __name__ == "__main__":
    s = Solution()
    print(s.longestCommonPrefix(["flower", "flow", "flight"]))
    print(s.longestCommonPrefix(["dog", "racecar", "car"]))

```

## Код:
```python
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        # for i in range(len(s) // 2):
        #     s[i], s[len(s) - 1 - i] = s[len(s) - 1 - i], s[i]
        s.reverse()
        return " ".join(s)


if __name__ == "__main__":
    s = Solution()
    print(s.reverseWords("the sky is blue"))
    print(s.reverseWords("  hello world  "))
    print(s.reverseWords("a good   example"))

```

## Код:
```python
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        strings = [""] * numRows
        count = 0
        up_flag = True

        for char in s:
            if up_flag:
                strings[count] += char
                count += 1
                if count >= numRows:
                    up_flag = False
                    count -= 2
            else:
                strings[count] += char
                count -= 1
                if count <= -1:
                    up_flag = True
                    count += 2
        return "".join(strings)


if __name__ == "__main__":
    s = Solution()
    print(s.convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR")
    print(s.convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI")
    print(s.convert("A", 1) == "A")

```

## Код:
```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


if __name__ == "__main__":
    s = Solution()
    print(s.strStr("sadbutsad", "sad"))
    print(s.strStr("leetcode", "leeto"))

```

## Код:
```python
from typing import List


class Solution:
    def fullJustify(self, strs: List[str], maxWidth: int) -> List[str]:
        result = []
        tmp_string = ""
        length = 0
        for string in strs:
            if len(string) + length > maxWidth:
                result.append(tmp_string.strip())
                tmp_string = string + " "
                length = len(string) + 1
            else:
                tmp_string += string + " "
                length += len(string) + 1
        if tmp_string != "":
            result.append(tmp_string.strip())

        for i in range(len(result)):
            if i != len(result) - 1:
                result[i] = self.justify(result[i], maxWidth)
            else:
                result[i] = result[i] + " " * (maxWidth - len(result[i]))

        return result

    def justify(self, line, width):
        words = line.split(" ")
        space_num = line.count(" ")
        empty = width - (len(line) - space_num)
        full_spaces = empty // space_num if space_num != 0 else empty
        spaces_need_to_add = empty % space_num if space_num != 0 else empty

        if len(words) == 1:
            return words[0] + " " * (width - len(words[0]))
        result = words[0]
        for i in range(1, len(words)):
            if spaces_need_to_add > 0:
                space = " " * (full_spaces + 1)
                spaces_need_to_add -= 1
            else:
                space = " " * full_spaces
            result += space + words[i]

        return result


if __name__ == "__main__":
    s = Solution()
    print(
        s.fullJustify(
            ["This", "is", "an", "example", "of", "text", "justification."], 16
        )
    )
    print(
        s.fullJustify(
            ["What", "must", "be", "acknowledgment", "shall", "be"], 16
        )
    )
    print(
        s.fullJustify(
            [
                "Science",
                "is",
                "what",
                "we",
                "understand",
                "well",
                "enough",
                "to",
                "explain",
                "to",
                "a",
                "computer.",
                "Art",
                "is",
                "everything",
                "else",
                "we",
                "do",
            ],
            20,
        )
    )
    print(
        s.fullJustify(["Listen", "to", "many,", "speak", "to", "a", "few."], 6)
    )

```

