
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        strings = [""] * numRows
        count = 0
        up_flag = True

        for char in s:
            if up_flag:
                strings[count] += char
                count += 1
                if count >= numRows:
                    up_flag = False
                    count -= 2
            else:
                strings[count] += char
                count -= 1
                if count <= -1:
                    up_flag = True
                    count += 2
        return "".join(strings)


if __name__ == "__main__":
    s = Solution()
    print(s.convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR")
    print(s.convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI")
    print(s.convert("A", 1) == "A")