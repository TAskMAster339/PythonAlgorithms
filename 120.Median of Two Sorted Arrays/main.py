class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        m, n = len(nums1), len(nums2)
        left, right = 0, m
        while left <= right:
            partition1 = (left + right) // 2
            partition2 = (m + n + 1) // 2 - partition1

            nums1_left_max = float("-inf") if partition1 == 0 else nums1[partition1 - 1]
            nums1_right_min = float("inf") if partition1 == m else nums1[partition1]
            nums2_left_max = float("-inf") if partition2 == 0 else nums2[partition2 - 1]
            nums2_right_min = float("inf") if partition2 == n else nums2[partition2]

            if nums1_left_max <= nums2_right_min and nums2_left_max <= nums1_right_min:
                if (m + n) % 2 == 0:
                    return (
                        max(nums1_left_max, nums2_left_max)
                        + min(nums1_right_min, nums2_right_min)
                    ) / 2
                return max(nums1_left_max, nums2_left_max)
            if nums1_left_max > nums2_right_min:
                right = partition1 - 1
            else:
                left = partition1 + 1
        return None


if __name__ == "__main__":
    f = Solution().findMedianSortedArrays
    print(f([1, 3], [2]))  # 2.0
    print(f([1, 2], [3, 4]))  # 2.5
    print(f([1, 3, 5, 7, 9], [2, 4, 6, 8, 10]))  # 5.5
