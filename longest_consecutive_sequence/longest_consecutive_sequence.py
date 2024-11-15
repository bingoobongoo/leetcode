class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        
        sorted_nums_unique = sorted(list(set(nums)))
        print(sorted_nums_unique)
        max_ctr = 1
        ctr = 1
        for i in range(1, len(sorted_nums_unique)):
            if sorted_nums_unique[i] == sorted_nums_unique[i-1] + 1:
                ctr += 1
            else:
                if ctr > max_ctr:
                    max_ctr = ctr
                ctr = 1
        
        if ctr > max_ctr:
            max_ctr = ctr
        
        return max_ctr
                
        
obj = Solution()
ans = obj.longestConsecutive([100,4,200,1,3,2])
print(ans)