from typing import List


class Solution:
    def fullJustify(self, strs: List[str], maxWidth: int) -> List[str]:
        result = []
        tmp_string = ""
        length = 0
        for string in strs:
            if len(string) + length > maxWidth:
                result.append(tmp_string.strip())
                tmp_string = string + " "
                length = len(string) + 1
            else:
                tmp_string += string + " "
                length += len(string) + 1
        if tmp_string != "":
            result.append(tmp_string.strip())

        for i in range(len(result)):
            if i != len(result) - 1:
                result[i] = self.justify(result[i], maxWidth)
            else:
                result[i] = result[i] + " " * (maxWidth - len(result[i]))

        return result

    def justify(self, line, width):
        words = line.split(" ")
        space_num = line.count(" ")
        empty = width - (len(line) - space_num)
        full_spaces = empty // space_num if space_num != 0 else empty
        spaces_need_to_add = empty % space_num if space_num != 0 else empty

        if len(words) == 1:
            return words[0] + " " * (width - len(words[0]))
        result = words[0]
        for i in range(1, len(words)):
            if spaces_need_to_add > 0:
                space = " " * (full_spaces + 1)
                spaces_need_to_add -= 1
            else:
                space = " " * full_spaces
            result += space + words[i]

        return result


if __name__ == "__main__":
    s = Solution()
    print(
        s.fullJustify(
            ["This", "is", "an", "example", "of", "text", "justification."], 16
        )
    )
    print(
        s.fullJustify(
            ["What", "must", "be", "acknowledgment", "shall", "be"], 16
        )
    )
    print(
        s.fullJustify(
            [
                "Science",
                "is",
                "what",
                "we",
                "understand",
                "well",
                "enough",
                "to",
                "explain",
                "to",
                "a",
                "computer.",
                "Art",
                "is",
                "everything",
                "else",
                "we",
                "do",
            ],
            20,
        )
    )
    print(
        s.fullJustify(["Listen", "to", "many,", "speak", "to", "a", "few."], 6)
    )
