import re

class Solution:
    def isValid(self, s: str) -> bool:
        if len(re.findall(r"(?:\(|\)|\[|\]|\{|\})", s)) % 2 != 0:
            return False

        stack = []
        char_table = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        for character in s:
            if character in char_table:
                if stack and stack[-1] == char_table[character]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(character)

        return stack == []


if __name__ == "__main__":
    s = Solution()

    print(s.isValid("()[]{}"))
    print(s.isValid("(]"))
    print(s.isValid("(]]"))
