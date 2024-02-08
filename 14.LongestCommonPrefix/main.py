class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        lcp = ''
        for i in range(len(strs[0])):
            for string in strs:
                if not string.startswith(strs[0][0:i+1]):
                    return lcp
            lcp += strs[0][i]
        return lcp
                
                    

obj = Solution()
print(obj.longestCommonPrefix(['']))
