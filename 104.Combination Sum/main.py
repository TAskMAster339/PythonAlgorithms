class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []

        def backtrack(comb: list[int], summary: int, level: int):
            if summary > target:
                return
            if summary == target:
                result.append(comb[:])
                return
            for i in range(level, len(candidates)):
                comb.append(candidates[i])
                backtrack(comb, summary + candidates[i], i)
                comb.pop()

        backtrack([], 0, 0)
        return result


if __name__ == "__main__":
    f = Solution().combinationSum
    print(f([2, 3, 6, 7], 7))
    print(f([2, 3, 5], 8))
    print(f([2], 1))
