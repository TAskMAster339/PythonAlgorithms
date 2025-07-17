class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []

        def backtrack(start):
            if start == len(nums):
                result.append(nums[:])
                return

            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]

        backtrack(0)
        return result


if __name__ == "__main__":
    f = Solution().permute
    print(f([1, 2, 3]))
    print(f([0, 1]))
    print(f([1]))
