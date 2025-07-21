class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []
        comb = []

        def backtrack(num: int, comb: list[str]):
            if len(comb) == 2 * n:
                result.append("".join(comb))
                return

            if num < n:
                comb.append("(")
                backtrack(num + 1, comb)
                comb.pop()
            if num * 2 != len(comb):
                comb.append(")")
                backtrack(num, comb)
                comb.pop()

        backtrack(0, comb)
        return result


if __name__ == "__main__":
    f = Solution().generateParenthesis
    print(f(3))
    print(f(1))
