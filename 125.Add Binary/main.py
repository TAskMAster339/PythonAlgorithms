class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        result = []
        while i >= 0 or j >= 0:
            if i < 0:
                summary = int(b[j]) + carry
                carry = summary // 2
                result.append(str(summary % 2))
                j -= 1
            elif j < 0:
                summary = int(a[i]) + carry
                carry = summary // 2
                result.append(str(summary % 2))
                i -= 1
            else:
                summary = int(a[i]) + int(b[j]) + carry
                carry = summary // 2
                result.append(str(summary % 2))
                i -= 1
                j -= 1
        if carry:
            result.append("1")
        return "".join(reversed(result))


if __name__ == "__main__":
    f = Solution().addBinary
    print(f("11", "1"))  # "100"
    print(f("1010", "1011"))  # "10101"
