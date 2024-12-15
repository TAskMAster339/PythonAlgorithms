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
    print(s.twoSum([5,25,75], 100))
