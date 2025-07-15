class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        result = []

        def backtack(num: int, word: list[str]):
            if len(word) == len(digits):
                result.append("".join(word))
                return
            for char in mapping[digits[num]]:
                word.append(char)
                backtack(num + 1, word)
                word.pop()

        backtack(0, [])
        return result


if __name__ == "__main__":
    f = Solution().letterCombinations
    print(f("23"))
    print(f(""))
    print(f("2"))
