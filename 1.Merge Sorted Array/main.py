from typing import List


class Solution:
    def merge(
        self, nums1: List[int], m: int, nums2: List[int], n: int
    ) -> None:
        m, n, i = m - 1, n - 1, m + n - 1
        while n >= 0:
            if m >= 0 and nums1[m] > nums2[n]:
                nums1[i] = nums1[m]
                m -= 1
            else:
                nums1[i] = nums2[n]
                n -= 1
            i -= 1


if __name__ == "__main__":
    s = Solution()
    s.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
    s.merge([1], 1, [], 0)
    s.merge([0], 0, [1], 1)
    s.merge([1, 0], 1, [2], 1)
