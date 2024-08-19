from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        map = {}

        for i in range(len(nums)):
            if map.get(nums[i]):
                map[nums[i]] += 1
                nums[i] = "_"
            else:
                map[nums[i]] = 1

        nums.sort(key=lambda x: 1 if x == "_" else 0)
        return len(map.keys())
