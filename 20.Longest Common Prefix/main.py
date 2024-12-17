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
