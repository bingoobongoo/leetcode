class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split()
        return len(s[-1])

obj = Solution()
test = obj.lengthOfLastWord('Hello World')
print(test)