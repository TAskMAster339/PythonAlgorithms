
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        # for i in range(len(s) // 2):
        #     s[i], s[len(s) - 1 - i] = s[len(s) - 1 - i], s[i]
        s.reverse()
        return " ".join(s)


if __name__ == "__main__":
    s = Solution()
    print(s.reverseWords("the sky is blue"))
    print(s.reverseWords("  hello world  "))
    print(s.reverseWords("a good   example"))