

class Solution:
    def intToRoman(self, num: int) -> str:
        table = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I",
        }
        result = ""
        for i in table.keys():
            while num >= i:
                num -= i
                result += table[i]
            # n = num // i
            # num %= i
            # result += (table[i] * n)

        return result


if __name__ == "__main__":
    s = Solution()
    print(s.intToRoman(3749))
    print(s.intToRoman(58))
    print(s.intToRoman(1994))
