class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        if len(s) == 1:
            return 1
        for i in range(len(s)):
            seen = []
            length = 0
            print(seen)
            for char in s[i:]:
                print(char)
                if char not in seen:
                    length += 1
                    seen.append(char)
                else:
                    break
            if length > maxLength:
                maxLength = length
            
        return maxLength
