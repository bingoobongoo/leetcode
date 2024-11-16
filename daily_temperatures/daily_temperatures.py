class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        min_temp = 30
        max_temp = 100
        temp_dict = {}
        ans = []
        for i in range(min_temp, max_temp+1):
            temp_dict[i] = None
        
        ans.append(0)
        for i in range(min_temp, temperatures[-1]):
            temp_dict[i] = len(temperatures) - 1
        
        i = len(temperatures) - 2
        while i >= 0:
            for temp in range(min_temp, temperatures[i]):
                temp_dict[temp] = i
        
            if (temperatures[i] < temperatures[i+1]):
                ans.append(1)
            else:
                next_higher_temp_idx = temp_dict[temperatures[i]]
                if next_higher_temp_idx == None:
                    ans.append(0)
                else:
                    ans.append(next_higher_temp_idx - i)
            i -= 1
        
        ans.reverse()
        return ans

obj = Solution()
ans = obj.dailyTemperatures([30,60,90])
print(ans)