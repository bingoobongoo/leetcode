# F**K THIS SHIT
# class Solution:
#     def halfMin(self, half: list[int]) -> int:
#         if len(half) == 1:
#             return half[0]
#         low = 0
#         high = len(half) - 1
#         first = half[low]
#         last = half[high]
#         min_num = 10000
#         while low <= high:
#             middle = low + (high - low) // 2
#             if half[middle] < min_num:
#                 min_num = half[middle]
#             if low == high:
#                 return min_num
#             if first < last:
#                 high = middle - 1
#                 last = half[high]
#             else:
#                 low = middle + 1
#                 first = half[low]
#         return min_num
#     def findMin(self, nums: list[int]) -> int:
#         if len(nums) == 1:
#             return nums[0]
#         low = 0
#         high = len(nums) - 1
#         middle = low + (high - low) // 2
#         min_left = self.halfMin(nums[:middle+1])
#         min_right = self.halfMin(nums[middle:])
        
#         return min(min_left, min_right)

class Solution:
    def findMin(self, nums: list[int]) -> int:
        return(sorted(nums)[0])

obj = Solution()
ans = obj.findMin([5,1,2,3,4])
print(ans)