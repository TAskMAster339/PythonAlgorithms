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
