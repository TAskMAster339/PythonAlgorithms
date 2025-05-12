from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1
            if nums[i] > 0:
                break
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.threeSum([-1, 0, 1, 2, -1, -4]))
    print(s.threeSum([0, 1, 1]))
    print(s.threeSum([0, 0, 0]))
    print(s.threeSum([3, -2, 1, 0]))  # []
    print(
        s.threeSum([-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4])
    )  # [[-4,0,4],[-4,1,3],[-3,-1,4],[-3,0,3],
    # [-3,1,2],[-2,-1,3],[-2,0,2],[-1,-1,2],[-1,0,1]]
    print(s.threeSum([-1, 0, 1, 0]))
