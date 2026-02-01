class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""

        for i in range(len(s)):
            start, end = i, i

            while end < len(s) and start > -1 and s[start] == s[end]:
                start -= 1
                end += 1

            longest = s[start + 1 : end]
            if len(longest) > len(result):
                result = longest

            start, end = i, i + 1

            while end < len(s) and start > -1 and s[start] == s[end]:
                start -= 1
                end += 1

            longest = s[start + 1 : end]
            if len(longest) > len(result):
                result = longest

        return result


if __name__ == "__main__":
    f = Solution().longestPalindrome
    print(f("babad"))  # "bab"
    print(f("cbbd"))  # "bb"
