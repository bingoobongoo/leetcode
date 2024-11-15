class Solution:
    def product(self, nums: list[int]) -> int:
        prod = 1
        for num in nums:
            prod *= num
        return prod
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        ans = []
        products = {}
        for (i, num) in list(enumerate(nums)):
            if i == 0:
                products[i] = (1, self.product(nums[i+1:]))
            else:
                if nums[i] == 0:
                    products[i] = (products[i-1][0]*nums[i-1], self.product(nums[i+1:]))
                else:
                    products[i] = (products[i-1][0]*nums[i-1], products[i-1][1]/nums[i])
            
            ans.append(self.product(products[i])) 
        
        ans = [int(a) for a in ans]
                
        return ans

obj = Solution()
print(obj.productExceptSelf([-1,1,0,-3,3]))