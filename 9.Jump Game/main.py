from typing import List



class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        target = 0
        zero_flag = False
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] == 0 and not zero_flag:
                target = 2
                zero_flag = True
            elif target != 0:
                if nums[i] >= target:
                    target = 0
                    zero_flag = False
                else:
                    target += 1
        return target == 0


if __name__ == "__main__":
    s = Solution()
    print(s.canJump([2,3,1,1,4]))
    print(s.canJump([3,2,1,0,4]))
    print(s.canJump([0,2,3]))
    print(s.canJump([2,0,1,0,1]))
    print(s.canJump([3,0,0,0]))
    print(s.canJump([1,0,0,1,1,2,2,0,2,2]))

