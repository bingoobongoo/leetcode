class Solution:
    def check(self, nums):
        for i in range (len(nums)):
            if nums == sorted(nums):
                return True
            nums= nums[1: ] + [nums[0]]
        return False

obj = Solution()
print(obj.check([1,2,3]))
