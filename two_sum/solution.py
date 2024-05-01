class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        numbers_complement: dict[int, int] = {}

        for idx, n in enumerate(nums):
            complement = numbers_complement.get(n, None)

            if complement is not None:
                return [complement, idx]

            numbers_complement[target - n] = idx
