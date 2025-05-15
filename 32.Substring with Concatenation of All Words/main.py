from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_len = len(words[0])
        etalon = dict()
        answer = []

        for word in words:
            if word in etalon:
                etalon[word] += 1
            else:
                etalon[word] = 1

        for i in range(word_len):
            start = i
            count = 0
            window = dict()
            for j in range(i, len(s) - word_len + 1, word_len):
                word = s[j : j + word_len]
                if word not in words:
                    start = j + word_len
                    window.clear()
                    count = 0
                    continue

                count += 1

                if word in window:
                    window[word] += 1
                else:
                    window[word] = 1

                while window[word] > etalon[word]:
                    window[s[start : start + word_len]] -= 1
                    start += word_len
                    count -= 1

                if count == len(words):
                    answer.append(start)
        return answer


if __name__ == "__main__":
    s = Solution()
    print(s.findSubstring("barfoothefoobarman", ["foo", "bar"]))
    print(
        s.findSubstring(
            "wordgoodgoodgoodbestword",
            ["word", "good", "best", "word"],
        ),
    )
    print(s.findSubstring("barfoofoobarthefoobarman", ["bar", "foo", "the"]))
    print(
        s.findSubstring(
            "wordgoodgoodgoodbestword",
            ["word", "good", "best", "good"],
        ),
    )
    print(
        s.findSubstring(
            "lingmindraboofooowingdingbarrwingmonkeypoundcake",
            ["fooo", "barr", "wing", "ding", "wing"],
        ),
    )
