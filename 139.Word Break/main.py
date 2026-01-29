class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        dp = [True] + [False] * len(s)

        for i in range(1, len(s) + 1):
            for w in wordDict:
                start = i - len(w)
                if start >= 0 and dp[start] and s[start:i] == w:
                    dp[i] = True
                    break

        return dp[-1]


if __name__ == "__main__":
    f = Solution().wordBreak
    print(f("leetcode", ["leet", "code"]))  # True
    print(f("applepenapple", ["apple", "pen"]))  # True
    print(f("catsandog", ["cats", "dog", "sand", "and", "cat"]))  # False
    print(f("aaaaaaa", ["aaaa", "aaa"]))  # True
