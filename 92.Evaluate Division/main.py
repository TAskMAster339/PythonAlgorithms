class Solution:
    def calcEquation(
        self,
        equations: list[list[str]],
        values: list[float],
        queries: list[list[str]],
    ) -> list[float]:

        graph = {}
        for i in range(len(equations)):
            node_start = equations[i][0]
            node_end = equations[i][1]
            if node_start not in graph:
                graph[node_start] = []
            if node_end not in graph:
                graph[node_end] = []
            graph[node_start].append((node_end, values[i]))
            graph[node_end].append((node_start, 1 / values[i]))


        def dfs(start: str, target: str, visited: set, path: float) -> float:
            if start == target:
                return path

            visited.add(start)
            for node, path_len in graph[start]:
                if node not in visited:
                    result = dfs(node, target, visited, path*path_len)
                    if result != -1:
                        return result
            return -1

        result = []
        for start, target in queries:
            if start not in graph or target not in graph:
                result.append(-1.0)
            elif start == target:
                result.append(1.0)
            else:
                visited = set()
                result.append(dfs(start, target, visited, 1))

        return result

if __name__ == "__main__":
    s = Solution()
    print(s.calcEquation(
        [["a","b"],["b","c"]],
        [2.0,3.0],
        [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]],
    ))
