from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        total_prefix = ""

        strs.sort()

        i = 0
        while True:
            if i == len(strs[0]) or i == len(strs[-1]):
                break
            if strs[0][i] == strs[-1][i]:
                total_prefix += strs[0][i]
                i += 1
                continue
            break

        return total_prefix

if __name__ == "__main__":
    s = Solution()

    print(s.longestCommonPrefix(["flower", "flowery", "floweryest"]))
