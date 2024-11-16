class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0
        
        while left < right:
            lower = None
            area = None
            if height[left] >= height[right]:
                lower = height[right]
                area = lower * (right-left)
                right -= 1
            else:
                lower = height[left]
                area = lower * (right-left)
                left += 1
            if area > max_area:
                max_area = area
            
        return max_area

obj = Solution()
ans = obj.maxArea([1,8,6,2,5,4,8,3,7])
print(ans)