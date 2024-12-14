
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True

        index = 0

        for i in range(len(t)):
            char = t[i]
            if index < len(s) and char == s[index]:
                index += 1
            if index == len(s):
                return True

        return False


if __name__ == "__main__":
    s = Solution()
    print(s.isSubsequence("abc", "ahbgdc"))
    print(s.isSubsequence("axc", "ahbgdc"))
    print(s.isSubsequence("acb", "ahbgdc"))
    print(s.isSubsequence("ab", "baab"))
    print(s.isSubsequence("", ""))