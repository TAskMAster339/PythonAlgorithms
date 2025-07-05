class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        if len(prerequisites) == 0:
            return True

        graph = {}
        for start, end in prerequisites:
            if start not in graph:
                graph[start] = []
            graph[start].append(end)

        visited = set()

        def dfs(vert: int) -> bool:
            if vert not in graph:
                return True

            if vert in visited:
                return False

            visited.add(vert)

            for child in graph[vert]:
                if not dfs(child):
                    return False

            del graph[vert]
            return True

        return all(dfs(i) for i in range(numCourses))


if __name__ == "__main__":
    f = Solution().canFinish
    print(f(2, [[1, 0]]))  # true
    print(f(2, [[1, 0], [0, 1]]))  # false
    print(f(5, [[1, 4], [2, 4], [3, 1], [3, 2]]))  # true
