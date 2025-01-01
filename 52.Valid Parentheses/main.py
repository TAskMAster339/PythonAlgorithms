from util import test_case


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        map = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for char in s:
            if char in "([{":
                stack.append(char)
            else:
                if not stack:
                    return False
                else:
                    if map[char] != stack.pop():
                        return False
        return len(stack) == 0


if __name__ == "__main__":
    f = Solution().isValid
    test_case(f, True, s="()")
    test_case(f, True, "()[]{}")
    test_case(f, False, "(]")
    test_case(f, True, "([])")
