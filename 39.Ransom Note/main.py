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
