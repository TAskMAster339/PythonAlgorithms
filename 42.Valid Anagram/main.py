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
