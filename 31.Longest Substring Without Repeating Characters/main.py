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
