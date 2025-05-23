# [**66) Partition List**](https://leetcode.com/problems/partition-list/description/)

## **Условие:**

Дан указатель на начало односвязного списка **head** и значение **x**, нужно разбить список так, чтобы все узлы, значение которых меньше **x**, были в списке раньше всех узлов, значение которых больше или равно **x**.

При этом нужно сохранить исходный порядок узлов в списке.

## **Идея:**

Бинарное дерево.

## **Реализация:**

Создадим две болванки **less** и **more**, к которым мы будем приклеивать узлы, которые меньше или больше, чем **x**. Затем в цикле мы проходим по всем узлам, создаем их копии и присоединяем их к соответствующим спискам. (Можно не создавать копии, но при этом нужно будет учесть, что может возникнуть ссылка на саму себя). Затем остается грамотно объединить полученные списки в один и вернуть его. Так как эти списки были получены одним прямым проходом по исходному списку, то мы можем гарантировать, что порядок элементов будет сохранён.



## **Оценка:**

По времени мы затратим **O**(**N**), так как проходим по списку длинной **N**. По памяти мы затратим **O**(**N**), так как создаем копию каждого узла. Можно сократить до **O**(**1**), если разобраться с ссылками. Но я выбрал копирование, так как это гарантирует, что мы получаем новый уникальный объект. (Его нельзя будет менять с помощью изначального списка, что очень надежно).

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

## Код:
```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        result = ""
        for char in s:
            if char.isalnum():
                result += char
        return result == result[::-1]


if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome("A man, a plan, a canal: Panama"))
    print(s.isPalindrome("race a car"))
    print(s.isPalindrome(" "))

```

## Код:
```python
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True

        index = 0

        for i in range(len(t)):
            char = t[i]
            if index < len(s) and char == s[index]:
                index += 1
            if index == len(s):
                return True

        return False


if __name__ == "__main__":
    s = Solution()
    print(s.isSubsequence("abc", "ahbgdc"))
    print(s.isSubsequence("axc", "ahbgdc"))
    print(s.isSubsequence("acb", "ahbgdc"))
    print(s.isSubsequence("ab", "baab"))
    print(s.isSubsequence("", ""))

```

## Код:
```python
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        first = 0
        second = len(numbers) - 1
        while True:
            if numbers[first] + numbers[second] < target:
                first += 1
            elif numbers[first] + numbers[second] > target:
                second -= 1
            else:
                return [first + 1, second + 1]


if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9))
    print(s.twoSum([2, 3, 4], 6))
    print(s.twoSum([-1, 0], -1))
    print(s.twoSum([5, 25, 75], 100))

```

## Код:
```python
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        left, right = 0, len(height) - 1
        while left < right:
            maxArea = max(
                maxArea, min(height[left], height[right]) * (right - left)
            )
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxArea


if __name__ == "__main__":
    s = Solution()
    print(s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
    print(s.maxArea([1, 1]))

```

## Код:
```python
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1
            if nums[i] > 0:
                break
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.threeSum([-1, 0, 1, 2, -1, -4]))
    print(s.threeSum([0, 1, 1]))
    print(s.threeSum([0, 0, 0]))
    print(s.threeSum([3, -2, 1, 0]))  # []
    print(
        s.threeSum([-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4])
    )  # [[-4,0,4],[-4,1,3],[-3,-1,4],[-3,0,3],
    # [-3,1,2],[-2,-1,3],[-2,0,2],[-1,-1,2],[-1,0,1]]
    print(s.threeSum([-1, 0, 1, 0]))

```

## Код:
```python
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        cur_sum = nums[left]
        min_len = float("inf")

        while right != len(nums) - 1 or left != len(nums):
            if cur_sum >= target:
                min_len = min(min_len, right - left + 1)
                cur_sum -= nums[left]
                left += 1
                continue
            else:
                right += 1
                if right >= len(nums):
                    return min_len if min_len != float("inf") else 0
            cur_sum += nums[right]
        return min_len if min_len != float("inf") else 0


if __name__ == "__main__":
    s = Solution()
    print(s.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
    print(s.minSubArrayLen(4, [1, 4, 4]))
    print(s.minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]))
    print(s.minSubArrayLen(11, [1, 2, 3, 4, 5]))  # 3
    print(s.minSubArrayLen(7, [1, 1, 1, 1, 7]))

```

## Код:
```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        max_len = 0
        start = 0
        letter_set = {s[start]}

        for end in range(1, len(s)):
            while s[end] in letter_set:
                letter_set.remove(s[start])
                start += 1
            else:
                letter_set.add(s[end])
                max_len = max(max_len, end - start + 1)

        return max_len


if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb"))
    print(s.lengthOfLongestSubstring("bbbbb"))
    print(s.lengthOfLongestSubstring("pwwkew"))
    print(s.lengthOfLongestSubstring(" "))

```

## Код:
```python
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_len = len(words[0])
        etalon = dict()
        answer = []

        for word in words:
            if word in etalon:
                etalon[word] += 1
            else:
                etalon[word] = 1

        for i in range(word_len):
            start = i
            count = 0
            window = dict()
            for j in range(i, len(s) - word_len + 1, word_len):
                word = s[j : j + word_len]
                if word not in words:
                    start = j + word_len
                    window.clear()
                    count = 0
                    continue

                count += 1

                if word in window:
                    window[word] += 1
                else:
                    window[word] = 1

                while window[word] > etalon[word]:
                    window[s[start : start + word_len]] -= 1
                    start += word_len
                    count -= 1

                if count == len(words):
                    answer.append(start)
        return answer


if __name__ == "__main__":
    s = Solution()
    print(s.findSubstring("barfoothefoobarman", ["foo", "bar"]))
    print(
        s.findSubstring(
            "wordgoodgoodgoodbestword",
            ["word", "good", "best", "word"],
        ),
    )
    print(s.findSubstring("barfoofoobarthefoobarman", ["bar", "foo", "the"]))
    print(
        s.findSubstring(
            "wordgoodgoodgoodbestword",
            ["word", "good", "best", "good"],
        ),
    )
    print(
        s.findSubstring(
            "lingmindraboofooowingdingbarrwingmonkeypoundcake",
            ["fooo", "barr", "wing", "ding", "wing"],
        ),
    )

```

## Код:
```python
from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        char_table = defaultdict(int)

        for char in t:
            char_table[char] += 1

        remaining_chars = len(t)
        min_window = float("inf")
        result = ""
        start = 0

        for end in range(len(s)):
            char = s[end]
            if char_table[char] > 0:
                remaining_chars -= 1
            char_table[char] -= 1

            if remaining_chars == 0:
                while True:
                    first_char = s[start]
                    if char_table[first_char] == 0:
                        break
                    char_table[first_char] += 1
                    start += 1

                if end - start < min_window:
                    min_window = end - start
                    result = s[start : end + 1]

                char_table[s[start]] += 1
                remaining_chars += 1
                start += 1

        return result


if __name__ == "__main__":
    s = Solution()
    print(s.minWindow("ADOBECODEBANC", "ABC"))
    print(s.minWindow("a", "a"))
    print(s.minWindow("a", "aa"))

```

## Код:
```python
from typing import List
from util import timer


class Solution:
    @timer
    def isValidSudoku2(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        cubes = [set() for _ in range(9)]

        for row in range(9):
            for column in range(9):
                item = board[row][column]

                if item == ".":
                    continue

                cube_index = 3 * (row // 3) + column // 3
                if (
                    item in rows[row]
                    or item in columns[column]
                    or item in cubes[cube_index]
                ):
                    return False

                rows[row].add(item)
                columns[column].add(item)
                cubes[cube_index].add(item)

        return True

    @timer
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return (
            self.vertical_check(board)
            and self.horizontal_check(board)
            and self.cube_check(board)
        )

    def vertical_check(self, board: List[List[str]]) -> bool:
        num_count = [0] * 10
        for i in range(len(board)):
            line = board[i]
            for item in line:
                if item == ".":
                    continue
                num_count[int(item)] += 1
            if any(elem > 1 for elem in num_count):
                return False
            else:
                num_count = [0] * 10
        return True

    def horizontal_check(self, board: List[List[str]]) -> bool:
        num_count = [0] * 10
        for i in range(9):
            for line in board:
                item = line[i]
                if item == ".":
                    continue
                num_count[int(item)] += 1

            if any(elem > 1 for elem in num_count):
                return False
            else:
                num_count = [0] * 10
        return True

    def cube_check(self, board: List[List[str]]) -> bool:
        num_count = [0] * 10

        for i in range(0, len(board), 3):
            count = 0
            for line in board:
                item1 = line[i]
                item2 = line[i + 1]
                item3 = line[i + 2]
                count += 3
                if item1.isnumeric():
                    num_count[int(item1)] += 1
                if item2.isnumeric():
                    num_count[int(item2)] += 1
                if item3.isnumeric():
                    num_count[int(item3)] += 1
                if count == 9:
                    if any(elem > 1 for elem in num_count):
                        return False
                    else:
                        num_count = [0] * 10
                        count = 0
        return True


if __name__ == "__main__":
    s = Solution()
    print("First example")
    print(
        s.isValidSudoku(
            [
                ["5", "3", ".", ".", "7", ".", ".", ".", "."],
                ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                [".", "9", "8", ".", ".", ".", ".", "6", "."],
                ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                [".", "6", ".", ".", ".", ".", "2", "8", "."],
                [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                [".", ".", ".", ".", "8", ".", ".", "7", "9"],
            ]
        )
    )  # True
    print(
        s.isValidSudoku2(
            [
                ["5", "3", ".", ".", "7", ".", ".", ".", "."],
                ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                [".", "9", "8", ".", ".", ".", ".", "6", "."],
                ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                [".", "6", ".", ".", ".", ".", "2", "8", "."],
                [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                [".", ".", ".", ".", "8", ".", ".", "7", "9"],
            ]
        )
    )  # True
    print("\nSecond example")
    print(
        s.isValidSudoku(
            [
                ["8", "3", ".", ".", "7", ".", ".", ".", "."],
                ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                [".", "9", "8", ".", ".", ".", ".", "6", "."],
                ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                [".", "6", ".", ".", ".", ".", "2", "8", "."],
                [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                [".", ".", ".", ".", "8", ".", ".", "7", "9"],
            ]
        )
    )  # False
    print(
        s.isValidSudoku2(
            [
                ["8", "3", ".", ".", "7", ".", ".", ".", "."],
                ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                [".", "9", "8", ".", ".", ".", ".", "6", "."],
                ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                [".", "6", ".", ".", ".", ".", "2", "8", "."],
                [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                [".", ".", ".", ".", "8", ".", ".", "7", "9"],
            ]
        )
    )  # False

```

## Код:
```python
from typing import List

from util import test_case


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows, columns = len(matrix), len(matrix[0])
        x, y, dx, dy = 0, 0, 1, 0
        result = []

        for k in range(rows * columns):
            result.append(matrix[y][x])
            matrix[y][x] = "*"

            if (
                not 0 <= x + dx < columns
                or not 0 <= y + dy < rows
                or matrix[y + dy][x + dx] == "*"
            ):
                dx, dy = -dy, dx

            x += dx
            y += dy

        return result


if __name__ == "__main__":
    s = Solution()
    test_case(
        s.spiralOrder,
        [1, 2, 3, 6, 9, 8, 7, 4, 5],
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    )
    test_case(
        s.spiralOrder,
        [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7],
        [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
    )

```

## Код:
```python
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for row in range(len(matrix)):
            for column in range(row, len(matrix[row])):
                matrix[row][column], matrix[column][row] = (
                    matrix[column][row],
                    matrix[row][column],
                )
        for row in matrix:
            row.reverse()


if __name__ == "__main__":
    s = Solution()
    mat1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    s.rotate(mat1)
    print(mat1)
    mat2 = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    s.rotate(mat2)
    print(mat2)

```

## Код:
```python
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][j] = "0"

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "0":
                    matrix[i][j] = 0
                    for ii in range(len(matrix)):
                        if matrix[ii][j] != "0":
                            matrix[ii][j] = 0
                    for jj in range(len(matrix[0])):
                        if matrix[i][jj] != "0":
                            matrix[i][jj] = 0


if __name__ == "__main__":
    s = Solution()
    mat1 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    s.setZeroes(mat1)
    print(mat1)
    mat2 = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    s.setZeroes(mat2)
    print(mat2)

```

## Код:
```python
from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        zero_sign = "*"
        one_sign = "$"

        for i in range(len(board)):
            for j in range(len(board[i])):
                count_one = 0
                for di in range(-1, 2):
                    for dj in range(-1, 2):
                        if -1 < i + di < len(board) and -1 < j + dj < len(
                            board[i]
                        ):
                            if di == 0 and dj == 0:
                                continue
                            if (
                                board[i + di][j + dj] == 1
                                or board[i + di][j + dj] == zero_sign
                            ):
                                count_one += 1

                if board[i][j] == 1:
                    if count_one < 2 or count_one > 3:
                        board[i][j] = zero_sign
                        continue
                if board[i][j] == 0:
                    if count_one == 3:
                        board[i][j] = one_sign
                        continue

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == zero_sign:
                    board[i][j] = 0
                if board[i][j] == one_sign:
                    board[i][j] = 1


if __name__ == "__main__":
    s = Solution()
    board1 = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
    s.gameOfLife(board1)
    Output1 = [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]
    print(board1)
    board2 = [[1, 1], [1, 0]]
    s.gameOfLife(board2)
    Output2 = [[1, 1], [1, 1]]
    print(board2)

```

## Код:
```python
from util import test_case


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        table = dict()
        for letter in magazine:
            if letter in table:
                table[letter] += 1
            else:
                table[letter] = 1

        for letter in ransomNote:
            if letter not in table.keys():
                return False
            if table[letter] == 0:
                return False
            table[letter] -= 1

        return True


if __name__ == "__main__":
    s = Solution()
    test_case(s.canConstruct, False, "a", "b")
    test_case(s.canConstruct, False, "aa", "ab")
    test_case(s.canConstruct, True, "aa", "aab")

```

## Код:
```python
from util import test_case


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        table = dict()
        for c in range(len(s)):
            char1 = s[c]
            char2 = t[c]
            if char1 not in table:
                if char2 in table.values():
                    return False
                table[char1] = char2
            else:
                if table[char1] != char2:
                    return False
        return True


if __name__ == "__main__":
    s = Solution().isIsomorphic
    test_case(s, True, "egg", "add")
    test_case(s, False, "foo", "bar")
    test_case(s, True, "paper", "title")
    test_case(s, False, "badc", "baba")
    test_case(s, False, "egcd", "adfd")

```

## Код:
```python
from util import test_case


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        table = dict()

        arr = s.split()
        if len(pattern) != len(arr):
            return False

        for i in range(len(arr)):
            word = arr[i]
            char = pattern[i]
            if char in table:
                if table[char] != word:
                    return False
            else:
                if word in table.values():
                    return False
                table[char] = word
        return True


if __name__ == "__main__":
    s = Solution().wordPattern
    test_case(s, True, "abba", "dog cat cat dog")
    test_case(s, False, "abba", "dog cat cat fish")
    test_case(s, False, "aaaa", "dog cat cat dog")
    test_case(s, False, "abba", "dog dog dog dog")

```

## Код:
```python
from util import test_case


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        table = dict()

        if len(t) != len(s):
            return False

        for char in s:
            if char in table:
                table[char] += 1
            else:
                table[char] = 1

        for char in t:
            if char not in table:
                return False
            table[char] -= 1
            if table[char] < 0:
                return False

        return True


if __name__ == "__main__":
    s = Solution().isAnagram
    test_case(s, True, s="anagram", t="nagaram")
    test_case(s, False, s="rat", t="car")

```

## Код:
```python
from typing import List
from util import test_case


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []

        i = 0
        index = 0
        while i < len(strs):
            if strs[i] == "000":
                i += 1
                continue
            etalon = dict()
            word = strs[i]

            for char in word:
                if char in etalon:
                    etalon[char] += 1
                else:
                    etalon[char] = 1
            result.append([word])
            strs[i] = "000"
            for j in range(i + 1, len(strs)):
                if strs[j] == "000" or len(strs[j]) != len(word):
                    continue
                table = dict()
                other_word = strs[j]

                for char in other_word:
                    if char in table:
                        table[char] += 1
                    else:
                        table[char] = 1

                if table == etalon:
                    result[index].append(other_word)
                    strs[j] = "000"
            i += 1
            index += 1
        return result

    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        result = dict()

        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in result:
                result[sorted_word].append(word)
            else:
                result[sorted_word] = [word]

        return list(result.values())


if __name__ == "__main__":
    s = Solution().groupAnagrams2
    test_case(
        s,
        [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]],
        ["eat", "tea", "tan", "ate", "nat", "bat"],
    )
    test_case(s, [[""]], [""])
    test_case(s, [["a"]], ["a"])

```

## Код:
```python
from typing import List
from util import test_case


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = dict()
        for i in range(len(nums)):
            table[nums[i]] = i

        for i in range(len(nums)):
            pair_element = target - nums[i]
            if pair_element in table and table[pair_element] != i:
                return [i, table[pair_element]]


if __name__ == "__main__":
    f = Solution().twoSum
    test_case(f, [0, 1], nums=[2, 7, 11, 15], target=9)
    test_case(f, [1, 2], nums=[3, 2, 4], target=6)
    test_case(f, [0, 1], nums=[3, 3], target=6)

```

## Код:
```python
from util.test import test_case


class Solution:
    def isHappy(self, n: int) -> bool:
        table = dict()

        while True:
            tmp = 0
            while n > 0:
                tmp += (n % 10) ** 2
                n //= 10
            if tmp in table:
                break
            else:
                table[tmp] = 1
            n = tmp

        return any(x == 1 for x in table.keys())


if __name__ == "__main__":
    f = Solution().isHappy
    test_case(f, True, 19)
    test_case(f, False, 2)

```

## Код:
```python
from typing import List
from util import test_case


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        table = dict()

        for i in range(len(nums)):
            if nums[i] in table:
                if i - table[nums[i]] <= k:
                    return True
            table[nums[i]] = i
        return False


if __name__ == "__main__":
    f = Solution().containsNearbyDuplicate
    test_case(f, True, nums=[1, 2, 3, 1], k=3)
    test_case(f, True, nums=[1, 0, 1, 1], k=1)
    test_case(f, False, [1, 2, 3, 1, 2, 3], k=2)

```

## Код:
```python
from typing import List
from util import test_case


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        table = {}
        result = 0
        for num in nums:
            left = table.get(num - 1, 0)
            right = table.get(num + 1, 0)
            length = left + right + 1
            table[num - left] = length
            table[num + right] = length
            result = max(result, length)
        return result


if __name__ == "__main__":
    f = Solution().longestConsecutive
    test_case(f, 4, nums=[100, 4, 200, 1, 3, 2])
    test_case(f, 9, nums=[0, 3, 7, 2, 5, 8, 4, 6, 0, 1])

```

## Код:
```python
from typing import List
from util import test_case


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        result = []
        left = 0
        right = 1
        while left != right:
            if right < len(nums) and nums[right] - nums[right - 1] > 1:
                if nums[left] == nums[right - 1]:
                    string = f"{nums[left]}"
                else:
                    string = f"{nums[left]}->{nums[right - 1]}"
                result.append(string)
                left = right
            if right <= len(nums) - 1:
                right += 1
            else:
                if nums[left] == nums[right - 1]:
                    string = f"{nums[left]}"
                else:
                    string = f"{nums[left]}->{nums[right - 1]}"
                result.append(string)
                left = right
        return result


if __name__ == "__main__":
    f = Solution().summaryRanges
    test_case(f, ["0->2", "4->5", "7"], [0, 1, 2, 4, 5, 7])
    test_case(f, ["0", "2->4", "6", "8->9"], [0, 2, 3, 4, 6, 8, 9])

```

## Код:
```python
from typing import List
from util import test_case


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:  # so bad
        intervals.sort(key=lambda arr: arr[0])
        left = 0
        right = 1
        while right < len(intervals):
            first = intervals[left]
            second = intervals[right]
            if second[0] <= first[1]:
                newLine = [first[0], max(second[1], first[1])]
                intervals.pop(right)
                intervals[left] = newLine
            else:
                left += 1
                right += 1
        return intervals

    def merge2(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i: i[0])
        output = [intervals[0]]

        for start, end in intervals[1:]:
            lastEnd = output[-1][1]
            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])
        return output


if __name__ == "__main__":
    f = Solution().merge
    test_case(
        f, [[1, 6], [8, 10], [15, 18]], [[1, 3], [2, 6], [8, 10], [15, 18]]
    )
    test_case(f, [[1, 5]], [[1, 4], [4, 5]])
    test_case(f, [[1, 3]], [[1, 3]])
    test_case(f, [[1, 4], [5, 6]], [[1, 4], [5, 6]])
    test_case(f, [[0, 5]], [[1, 4], [0, 2], [3, 5]])

```

## Код:
```python
from typing import List

from util import test_case


class Solution:
    def insert(
        self,
        intervals: List[List[int]],
        newInterval: List[int],
    ) -> List[List[int]]:
        result = []
        i = 0

        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval = [
                min(newInterval[0], intervals[i][0]),
                max(newInterval[1], intervals[i][1]),
            ]
            i += 1
        result.append(newInterval)

        while i < len(intervals):
            result.append(intervals[i])
            i += 1

        return result


if __name__ == "__main__":
    f = Solution().insert
    test_case(
        f,
        [[1, 5], [6, 9]],
        intervals=[[1, 3], [6, 9]],
        newInterval=[2, 5],
    )
    test_case(
        f,
        [[1, 2], [3, 10], [12, 16]],
        intervals=[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]],
        newInterval=[4, 8],
    )
    test_case(f, [[1, 7]], [[1, 5]], [2, 7])

```

## Код:
```python
from typing import List
from util import test_case


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points.sort(key=lambda x: x[1])

        union = []
        start = points[0][0]
        end = points[0][1]
        for x, y in points[1:]:
            if end < x:
                union.append([start, end])
                start = 0
                end = float("inf")
            start = max(start, x)
            end = min(end, y)
        union.append([start, end])

        return len(union)

    def findMinArrowShots2(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points.sort(key=lambda x: x[1])
        prev = points[0]
        total = 1
        for i in points[1:]:
            if prev[1] < i[0]:
                prev = i
                total += 1
        return total


if __name__ == "__main__":
    f = Solution().findMinArrowShots2
    test_case(f, 2, points=[[10, 16], [2, 8], [1, 6], [7, 12]])
    test_case(f, 4, [[1, 2], [3, 4], [5, 6], [7, 8]])
    test_case(f, 2, points=[[1, 2], [2, 3], [3, 4], [4, 5]])
    test_case(f, 0, [])
    test_case(f, 2, [[1, 2], [4, 5], [1, 5]])
    test_case(
        f,
        2,
        [
            [3, 9],
            [7, 12],
            [3, 8],
            [6, 8],
            [9, 10],
            [2, 9],
            [0, 9],
            [3, 9],
            [0, 6],
            [2, 8],
        ],
    )

```

## Код:
```python
from util import test_case


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        map = {")": "(", "]": "[", "}": "{"}

        for char in s:
            if char in "([{":
                stack.append(char)
            else:
                if not stack:
                    return False
                else:
                    if map[char] != stack.pop():
                        return False
        return len(stack) == 0


if __name__ == "__main__":
    f = Solution().isValid
    test_case(f, True, s="()")
    test_case(f, True, "()[]{}")
    test_case(f, False, "(]")
    test_case(f, True, "([])")

```

## Код:
```python
from util import test_case


class Solution:
    def simplifyPath(self, path: str) -> str:
        path_words = path.split("/")
        stack = []
        for word in path_words:
            if not word:
                continue
            else:
                if word == ".":
                    continue
                elif word == "..":
                    if stack:
                        stack.pop()
                else:
                    stack.append(word)
        return "/" + "/".join(stack)


if __name__ == "__main__":
    f = Solution().simplifyPath
    test_case(f, "/home", path="/home/")
    test_case(f, "/home/foo", path="/home//foo/")
    test_case(f, "/home/user/Pictures", "/home/user/Documents/../Pictures")
    test_case(f, "/", "/../")
    test_case(f, "/.../b/d", "/.../a/../b/c/../d/./")

```

## Код:
```python
class MinStackNoMemo:
    def __init__(self):
        self.data = []
        self.min = float("inf")

    def push(self, val: int) -> None:
        self.data.append(val)
        if val < self.min:
            self.min = val

    def pop(self) -> None:
        elem = self.data.pop()
        if elem == self.min:
            if self.data:
                self.min = min(self.data)
            else:
                self.min = float("inf")

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.min


class MinStack:
    def __init__(self):
        self.data = []

    def push(self, val: int) -> None:
        if not self.data:
            self.data.append((val, val))
        else:
            self.data.append((val, min(val, self.data[-1][0])))

    def pop(self) -> None:
        self.data.pop()

    def top(self) -> int:
        return self.data[-1][0]

    def getMin(self) -> int:
        return self.data[-1][1]


if __name__ == "__main__":
    obj = MinStack()
    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    print(obj.getMin())
    obj.pop()
    print(obj.top())
    print(obj.getMin())

```

## Код:
```python
from typing import List
from util import test_case as tc


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            if i in "+-*/":
                elem2 = stack.pop()
                elem1 = stack.pop()
                match i:
                    case "+":
                        stack.append(elem1 + elem2)
                    case "-":
                        stack.append(elem1 - elem2)
                    case "*":
                        stack.append(elem1 * elem2)
                    case "/":
                        stack.append(int(elem1 / elem2))
            else:
                stack.append(int(i))
        return stack[0]


if __name__ == "__main__":
    f = Solution().evalRPN
    tc(f, 9, tokens=["2", "1", "+", "3", "*"])
    tc(f, 6, tokens=["4", "13", "5", "/", "+"])
    tc(
        f,
        22,
        ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"],
    )
    tc(f, -7, ["4", "-2", "/", "2", "-3", "-", "-"])

```

## Код:
```python
from util import test_case
from typing import List
import re


def evalRPN(tokens: List[str]) -> int:
    stack = []

    for i in tokens:
        if i in "+-":
            elem2 = stack.pop()
            elem1 = stack.pop()
            match i:
                case "+":
                    stack.append(elem1 + elem2)
                case "-":
                    stack.append(elem1 - elem2)
        else:
            stack.append(int(i))
    return stack[0]


class Solution:
    def calculate(self, s: str) -> int:
        RPN = []
        stack = []

        number = ""
        s = s.replace(" ", "")
        if s[0] == "-":
            s = "0" + s
        s = re.sub(r"\(-(\d+)", r"(0-\1", s)
        s = re.sub(r"\(-\(", r"(0-(", s)
        for i in range(len(s)):
            char = s[i]

            if char.isnumeric():
                number += char
            else:
                if number:
                    RPN.append(number)
                number = ""
                if char == "(":
                    stack.append(char)
                elif char == ")":
                    while stack and stack[-1] != "(":
                        RPN.append(stack.pop())
                    stack.pop()
                elif char in "+-":
                    while stack and stack[-1] in "+-":
                        RPN.append(stack.pop())
                    stack.append(char)
        if number:
            RPN.append(number)
        for item in reversed(stack):
            RPN.append(item)

        return evalRPN(RPN)


if __name__ == "__main__":
    f = Solution().calculate
    test_case(f, 2, s="1 + 1")
    test_case(f, 3, s=" 2-1 + 2 ")
    test_case(f, 23, s="(1+(4+5+2)-3)+(6+8)")
    test_case(f, 3, "1-(     -2)")
    test_case(f, -12, "- (3 - (- (4 + 5) ) )")

```

## Код:
```python
from typing import Optional
from util import test_case


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True

        return False


if __name__ == "__main__":
    start = ListNode(3)
    second = ListNode(2)
    third = ListNode(0)
    fourth = ListNode(5)
    last = ListNode(-4)
    start.next = second
    second.next = third
    third.next = fourth
    fourth.next = last
    last.next = second

    uno_lst = ListNode(1)
    f = Solution().hasCycle
    test_case(f, True, start)
    test_case(f, False, uno_lst)

```

## Код:
```python
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        returnList = ListNode(0)
        begin = returnList
        carry = 0

        while l1 or l2 or carry != 0:
            digit1 = l1.val if l1 else 0
            digit2 = l2.val if l2 else 0

            total = (digit1 + digit2 + carry) % 10
            carry = (digit1 + digit2 + carry) // 10

            newNode = ListNode(total)
            returnList.next = newNode
            returnList = returnList.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        result = begin.next
        begin.next = None
        begin = None
        return result


if __name__ == "__main__":
    first = ListNode(2)
    first2 = ListNode(4)
    first3 = ListNode(3)
    first.next = first2
    first2.next = first3

    second = ListNode(5)
    second2 = ListNode(6)
    second3 = ListNode(4)
    second.next = second2
    second2.next = second3

    f = Solution().addTwoNumbers(first, second)

    while f:
        print(f.val)
        f = f.next

```

## Код:
```python
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        newList = ListNode(0)
        begin = newList

        while list1 or list2:
            val1 = list1.val if list1 else float("inf")
            val2 = list2.val if list2 else float("inf")

            if val1 < val2:
                newList.next = ListNode(val1)
                list1 = list1.next if list1 else None
            elif val2 <= val1:
                newList.next = ListNode(val2)
                list2 = list2.next if list2 else None
            newList = newList.next

        result = begin.next
        begin.next = None
        begin = None
        return result


if __name__ == "__main__":
    list1 = ListNode(1, ListNode(2, ListNode(4)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))

    f = Solution().mergeTwoLists(list1, list2)
    while f:
        print(f.val)
        f = f.next

```

## Код:
```python
from typing import Optional


class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if not head:
            return None

        # Copy of all Nodes
        curr = head
        while curr:
            new_node = Node(curr.val, curr.next)
            curr.next = new_node
            curr = new_node.next

        curr = head
        # make new Random nodes connections
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        old_head = head
        new_head = head.next
        curr_old = old_head
        curr_new = new_head

        # Slice two lists
        while curr_old:
            curr_old.next = curr_old.next.next
            curr_new.next = curr_new.next.next if curr_new.next else None
            curr_old = curr_old.next
            curr_new = curr_new.next

        return new_head

```

## Код:
```python
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        if not head and left == right:
            return head

        result = ListNode(0, head)
        LeftPointer, current = result, head

        for i in range(left - 1):
            LeftPointer, current = current, current.next

        prevPointer = None
        for i in range(right - left + 1):
            nextNodePointer = current.next
            current.next = prevPointer
            prevPointer, current = current, nextNodePointer

        LeftPointer.next.next = current
        LeftPointer.next = prevPointer
        return result.next

```

## Код:
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverse(self, start, end):
        prev, curr = None, start
        while curr != end:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

    def reverseKGroup(self, head, k):
        count, temp = 0, head
        while temp and count < k:
            temp = temp.next
            count += 1
        if count < k:
            return head

        new_head = self.reverse(head, temp)
        head.next = self.reverseKGroup(temp, k)
        return new_head

```

## Код:
```python
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(
        self, head: Optional[ListNode], n: int
    ) -> Optional[ListNode]:
        fast_pointer = head

        for i in range(n):
            fast_pointer = fast_pointer.next

        if not fast_pointer:
            return head.next

        slow_pointer = head
        prev = None

        while fast_pointer:
            fast_pointer = fast_pointer.next
            prev = slow_pointer
            slow_pointer = slow_pointer.next

        prev.next = prev.next.next

        return head

```

## Код:
```python
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start = head
        if not start or start.next is None:
            return head

        left = start
        right = start.next
        prev = None

        while True:
            if left.val != right.val:
                prev = left
                left = right
                right = right.next
            else:
                while right and left.val == right.val:
                    right = right.next
                if prev:
                    prev.next = right
                    left = prev
                else:
                    left = right
                    if right:
                        right = right.next
                    start = left
            if not right:
                break
        return start

```

## Код:
```python
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(
        self,
        head: Optional[ListNode],
        k: int,
    ) -> Optional[ListNode]:
        end = head
        length = 1
        if not end or not end.next:
            return head

        while end.next:
            end = end.next
            length += 1

        k %= length

        if k == 0:
            return head

        start = head
        prev = None

        for i in range(length - k):
            prev = start
            start = start.next

        prev.next = None
        end.next = head
        return start

```

## Код:
```python
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(
        self,
        head: Optional[ListNode],
        x: int,
    ) -> Optional[ListNode]:
        less = ListNode()
        more = ListNode()

        start = less
        end = more

        while head:
            if head.val < x:
                less.next = ListNode(head.val)
                less = less.next
            else:
                more.next = ListNode(head.val)
                more = more.next
            head = head.next

        less.next = end.next
        return start.next

```

