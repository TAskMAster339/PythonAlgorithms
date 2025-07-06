from collections import defaultdict, deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        graph = defaultdict(list)

        in_degree = [0] * numCourses

        for u, v in prerequisites:
            in_degree[u] += 1
            graph[v].append(u)

        queue = deque([x for x in range(numCourses) if in_degree[x] == 0])
        result = []

        while queue:
            vert = queue.popleft()
            result.append(vert)
            for child in graph[vert]:
                in_degree[child] -= 1
                if in_degree[child] == 0:
                    queue.append(child)

        return result if len(result) == numCourses else []


if __name__ == "__main__":
    f = Solution().findOrder
    print(f(2, [[1, 0]]))
    print(f(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))
    print(f(1, []))
