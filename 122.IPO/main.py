import heapq


class Solution:
    def findMaximizedCapital(
        self,
        k: int,
        w: int,
        profits: list[int],
        capital: list[int],
    ) -> int:
        projects = [(capital[i], profits[i]) for i in range(len(profits))]
        projects.sort()
        priority_queue = []
        indx = 0
        for _ in range(k):
            while indx < len(profits) and projects[indx][0] <= w:
                heapq.heappush(priority_queue, -projects[indx][1])
                indx += 1
            if not priority_queue:
                break
            # Вычитаем так как, в очереди храняться отрицательные числа
            w -= heapq.heappop(priority_queue)

        return w


if __name__ == "__main__":
    f = Solution().findMaximizedCapital
    print(f(2, 0, [1, 2, 3], [0, 1, 1]))
    print(f(3, 0, [1, 2, 3], [0, 1, 2]))
