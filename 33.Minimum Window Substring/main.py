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
                    result = s[start: end + 1]

                char_table[s[start]] += 1
                remaining_chars += 1
                start += 1

        return result


if __name__ == "__main__":
    s = Solution()
    print(s.minWindow("ADOBECODEBANC", "ABC"))
    print(s.minWindow("a", "a"))
    print(s.minWindow("a", "aa"))
