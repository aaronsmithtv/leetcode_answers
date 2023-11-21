from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for each indice in list, compare it to every other index in list
        # remove the index from the list as we know it will not result
        target_nums = nums.copy()

        while target_nums:
            ind_num = target_nums.pop(0)
            for comp_num in target_nums:
                if ind_num + comp_num == target:
                    return [ind_num, comp_num]


if __name__ == "__main__":
    s = Solution()

    print(s.twoSum(nums=[2, 7, 11, 15], target=9))
