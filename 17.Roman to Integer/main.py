class Solution:
    def romanToInt(self, s: str) -> int:
        table = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        prev = s[0]
        result = table[s[0]]
        for i in range(1, len(s)):
            if table[s[i]] > table[prev]:
                #    result -= table[prev]
                result += table[s[i]] - 2 * table[prev]
            else:
                result += table[s[i]]
            prev = s[i]
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.romanToInt("III"))
    print(s.romanToInt("LVIII"))
    print(s.romanToInt("MCMXCIV"))
