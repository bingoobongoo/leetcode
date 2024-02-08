class Solution:
    def twoSum(self, nums: list[int], target: int) -> int:
        dictionary = {}
        for i, num in enumerate(nums):
            if target - num in dictionary:
                return [dictionary[target-num], i]
            elif num not in dictionary:
                dictionary[num] = i