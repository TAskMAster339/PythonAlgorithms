import heapq


class Solution:
    def kSmallestPairs(
        self,
        nums1: list[int],
        nums2: list[int],
        k: int,
    ) -> list[list[int]]:
        if not nums1 and not nums2:
            return []

        pq = []
        heapq.heappush(pq, (nums1[0] + nums2[0], 0, 0))
        visited = set()
        result = []

        while pq and len(result) < k:
            _, i, j = heapq.heappop(pq)
            result.append((nums1[i], nums2[j]))
            if i + 1 < len(nums1) and (i + 1, j) not in visited:
                heapq.heappush(pq, (nums1[i + 1] + nums2[j], i + 1, j))
                visited.add((i + 1, j))
            if j + 1 < len(nums2) and (i, j + 1) not in visited:
                heapq.heappush(pq, (nums1[i] + nums2[j + 1], i, j + 1))
                visited.add((i, j + 1))

        return result


if __name__ == "__main__":
    f = Solution().kSmallestPairs
    print(f([1, 7, 11], [2, 4, 6], 3))
    print(f([1, 1, 2], [1, 2, 3], 2))
