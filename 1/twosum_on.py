from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """Uses a hash table to look up the complement of the currently
        iterated number to see if a sum pair can be found.
        """
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement], i]
            else:
                seen[num] = i


if __name__ == "__main__":
    s = Solution()

    print(s.twoSum(nums=[3, 2, 7, 11, 15], target=9))
