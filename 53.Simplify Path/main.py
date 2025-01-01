from util import test_case


class Solution:
    def simplifyPath(self, path: str) -> str:
        path_words = path.split("/")
        stack = []
        for word in path_words:
            if not word:
                continue
            else:
                if word == ".":
                    continue
                elif word == "..":
                    if stack:
                        stack.pop()
                else:
                    stack.append(word)
        return "/" + "/".join(stack)


if __name__ == "__main__":
    f = Solution().simplifyPath
    test_case(f, "/home", path="/home/")
    test_case(f, "/home/foo", path="/home//foo/")
    test_case(f, "/home/user/Pictures", "/home/user/Documents/../Pictures")
    test_case(f, "/", "/../")
    test_case(f, "/.../b/d", "/.../a/../b/c/../d/./")
