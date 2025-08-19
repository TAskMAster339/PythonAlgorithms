class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        reversed_x = 0
        x_copy = x
        while x:
            reversed_x = reversed_x * 10 + x % 10
            x //= 10
        return x_copy == reversed_x


if __name__ == "__main__":
    f = Solution().isPalindrome
    print(f(121))  # True
    print(f(-121))  # False
    print(f(10))  # False
