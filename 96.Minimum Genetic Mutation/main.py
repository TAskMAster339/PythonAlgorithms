from collections import deque


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:
        if endGene not in bank and startGene != endGene:
            return -1

        def is_near(first_gene: str, second_gene: str) -> bool:
            count = 0
            for i in range(len(second_gene)):  # len(fisrt_gene) == len(second_gene)== 8
                if first_gene[i] != second_gene[i]:
                    count += 1
            return count == 1

        queue = deque()
        queue.append((startGene, 0))
        visited = set()

        while queue:
            gene, path_len = queue.popleft()
            if gene == endGene:
                return path_len
            visited.add(gene)
            for next_gene in bank:
                if next_gene not in visited and is_near(next_gene, gene):
                    queue.append((next_gene, path_len + 1))

        return -1


if __name__ == "__main__":
    f = Solution().minMutation
    print(f("AACCGGTT", "AACCGGTA", ["AACCGGTA"]))
    print(f("AACCGGTT", "AAACGGTA", ["AACCGGTA", "AACCGCTA", "AAACGGTA"]))
