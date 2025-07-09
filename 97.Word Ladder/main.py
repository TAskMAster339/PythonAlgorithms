from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        wordSet = set(wordList)

        if endWord not in wordSet:
            return 0

        queue = deque([(beginWord, 1)])

        while queue:
            word, path_len = queue.popleft()
            if word == endWord:
                return path_len
            for i in range(len(word)):
                for char in "abcdefghijklmnopqrstuvwxyz":
                    new_word = word[:i] + char + word[i + 1 :]
                    if new_word in wordSet:
                        wordSet.remove(new_word)
                        queue.append((new_word, path_len + 1))

        return 0


if __name__ == "__main__":
    f = Solution().ladderLength
    print(f("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
    print(f("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))
