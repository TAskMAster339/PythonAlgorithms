from util import test_case
from typing import List
import re


def evalRPN(tokens: List[str]) -> int:
    stack = []

    for i in tokens:
        if i in "+-":
            elem2 = stack.pop()
            elem1 = stack.pop()
            match i:
                case "+":
                    stack.append(elem1 + elem2)
                case "-":
                    stack.append(elem1 - elem2)
        else:
            stack.append(int(i))
    return stack[0]


class Solution:
    def calculate(self, s: str) -> int:
        RPN = []
        stack = []

        number = ""
        s = s.replace(" ", "")
        if s[0] == "-":
            s = "0" + s
        s = re.sub(r"\(-(\d+)", r"(0-\1", s)
        s = re.sub(r"\(-\(", r"(0-(", s)
        for i in range(len(s)):
            char = s[i]

            if char.isnumeric():
                number += char
            else:
                if number:
                    RPN.append(number)
                number = ""
                if char == "(":
                    stack.append(char)
                elif char == ")":
                    while stack and stack[-1] != "(":
                        RPN.append(stack.pop())
                    stack.pop()
                elif char in "+-":
                    while stack and stack[-1] in "+-":
                        RPN.append(stack.pop())
                    stack.append(char)
        if number:
            RPN.append(number)
        for item in reversed(stack):
            RPN.append(item)

        return evalRPN(RPN)


if __name__ == "__main__":
    f = Solution().calculate
    test_case(f, 2, s="1 + 1")
    test_case(f, 3, s=" 2-1 + 2 ")
    test_case(f, 23, s="(1+(4+5+2)-3)+(6+8)")
    test_case(f, 3, "1-(     -2)")
    test_case(f, -12, "- (3 - (- (4 + 5) ) )")
