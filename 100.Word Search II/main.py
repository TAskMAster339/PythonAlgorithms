from collections import deque


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end

    def is_prefix(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

    def delete(self, word: str) -> None:
        if not self.search(word):
            return

        nodes = []
        node = self.root
        for char in word:
            nodes.append((char, node))
            node = node.children[char]
        node.is_end = False

        for i in range(len(nodes) - 1, -1, -1):
            char, parent_node = nodes[i]
            current_node = parent_node.children[char]
            if not current_node.is_end and not current_node.children:
                del parent_node.children[char]
            else:
                break


class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        m = len(board)
        n = len(board[0])

        trie = Trie()
        for word in words:
            trie.insert(word)
        result = set()
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

        def dfs(r: int, c: int, path: str, visited: deque) -> None:
            if (r, c) in visited:
                return

            current_word = path + board[r][c]
            if not trie.is_prefix(current_word):
                return

            if trie.search(current_word):
                result.add(current_word)
                trie.delete(current_word)

            visited.append((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    dfs(nr, nc, current_word, visited)
            visited.pop()

        for i in range(m):
            for j in range(n):
                dfs(i, j, "", deque())

        return list(result)


if __name__ == "__main__":
    f = Solution().findWords
    print(  # ["eat","oath"]
        f(
            [
                ["o", "a", "a", "n"],
                ["e", "t", "a", "e"],
                ["i", "h", "k", "r"],
                ["i", "f", "l", "v"],
            ],
            ["oath", "pea", "eat", "rain"],
        ),
    )
    print(f([["a", "b"], ["c", "d"]], ["abcb"]))  # []
    print(f([["a", "a"]], ["aaa"]))  # []
    print(  # ["abcdefg","befa","eaabcdgfa","gfedcbaaa"]
        f(
            [
                ["a", "b", "c"],
                ["a", "e", "d"],
                ["a", "f", "g"],
            ],
            ["abcdefg", "gfedcbaaa", "eaabcdgfa", "befa", "dgc", "ade"],
        ),
    )
