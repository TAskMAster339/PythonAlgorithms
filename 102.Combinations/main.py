class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        result = []

        def backtrack(level: int, comb: list[int]):
            if len(comb) == k:
                result.append(comb[:])
                return
            for i in range(level, n + 1):
                comb.append(i)
                backtrack(i + 1, comb)
                comb.pop()

        backtrack(1, [])
        return result


if __name__ == "__main__":
    f = Solution().combine
    print(f(4, 2))
    print(f(1, 1))
    print(f(3, 3))
