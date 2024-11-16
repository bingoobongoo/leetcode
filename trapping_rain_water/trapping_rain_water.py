class Solution:
    def trap(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        trapped_water = 0
        current_height = 1
        
        while (left < right):
            while height[left] < current_height and left < right:
                left += 1
            while height[right] < current_height and left < right:
                right -= 1
            
            for i in range(left+1, right):
                if height[i] < current_height:
                    trapped_water += 1
            
            current_height += 1
            
        return trapped_water

obj = Solution()
ans = obj.trap()
print(ans)
            