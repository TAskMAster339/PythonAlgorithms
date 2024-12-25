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
