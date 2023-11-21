from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        total_prefix = ""

        for character in strs[0]:
            new_prefix = total_prefix + character
            sw_count = sum(
                map(
                    lambda i: i, (
                        1 for og_str in strs if og_str.startswith(new_prefix)
                    )
                )
            )
            if sw_count != len(strs):
                break
            total_prefix = new_prefix

        return total_prefix

if __name__ == "__main__":
    s = Solution()

    print(s.longestCommonPrefix(["dog", "racecar", "car"]))
