from util.test import test_case


class Solution:
    def isHappy(self, n: int) -> bool:
        table = dict()

        while True:
            tmp = 0
            while n > 0:
                tmp += (n % 10) ** 2
                n //= 10
            if tmp in table:
                break
            else:
                table[tmp] = 1
            n = tmp

        return any(x == 1 for x in table.keys())


if __name__ == "__main__":
    f = Solution().isHappy
    test_case(f, True, 19)
    test_case(f, False, 2)
