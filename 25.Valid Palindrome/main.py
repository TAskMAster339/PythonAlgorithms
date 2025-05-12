class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        result = ""
        for char in s:
            if char.isalnum():
                result += char
        return result == result[::-1]


if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome("A man, a plan, a canal: Panama"))
    print(s.isPalindrome("race a car"))
    print(s.isPalindrome(" "))
