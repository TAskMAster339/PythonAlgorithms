from typing import List
from util import test_case as tc


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            if i in "+-*/":
                elem2 = stack.pop()
                elem1 = stack.pop()
                match i:
                    case "+":
                        stack.append(elem1 + elem2)
                    case "-":
                        stack.append(elem1 - elem2)
                    case "*":
                        stack.append(elem1 * elem2)
                    case "/":
                        # signFlag = True
                        # if elem1 < 0 < elem2 or elem2 < 0 < elem1:
                        #     signFlag = False
                        # stack.append((elem1 // elem2) if signFlag else (-elem1 // elem2))
                        stack.append(int(elem1 / elem2))
            else:
                stack.append(int(i))
        return stack[0]


if __name__ == "__main__":
    f = Solution().evalRPN
    tc(f, 9, tokens=["2", "1", "+", "3", "*"])
    tc(f, 6, tokens=["4", "13", "5", "/", "+"])
    tc(f, 22, ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])
    tc(f, -7, ["4", "-2", "/", "2", "-3", "-", "-"])
