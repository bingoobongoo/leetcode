class Solution:
    def minSubarray(self, nums: list[int], p: int) -> int:
        remainder = sum(nums) % p

        if remainder == 0:
            return 0

        prefix_sums = [sum(nums[:i+1]) for i in range(len(nums))]
        return prefix_sums

obj = Solution()
print(obj.minSubarray([1,2,3], 4))
            
        