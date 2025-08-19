class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        i = len(digits) - 1
        carry = (digits[i] + 1) // 10
        digits[i] = (digits[i] + 1) % 10
        i -= 1
        while carry and i >= 0:
            carry = (digits[i] + 1) // 10
            digits[i] = (digits[i] + 1) % 10
            i -= 1
        if carry:
            return [1, *digits]
        return digits


if __name__ == "__main__":
    f = Solution().plusOne
    print(f([1, 2, 3]))  # [1, 2, 4]
    print(f([4, 3, 2, 1]))  # [4, 3, 2, 2]
    print(f([9]))  # [1, 0]
