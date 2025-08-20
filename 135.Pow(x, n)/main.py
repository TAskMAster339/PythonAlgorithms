class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            n = -n
            x = 1 / x
        result = 1
        while n > 0:
            if n & 1 == 1:
                result *= x
            x *= x
            n >>= 1
        return result


if __name__ == "__main__":
    f = Solution().myPow
    print(f(2, 10))  # 1024
    print(f(2.1, 3))  # 9.261
    print(f(2, -2))  # 0.25
