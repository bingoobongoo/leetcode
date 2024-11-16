class Solution:
    def isPalindrome(self, s: str) -> bool:
        stripped = []
        for char in s:
            if char.isalpha() or char.isnumeric():
                stripped.append(char)
        stripped = "".join(stripped)
        stripped = stripped.lower()
        rev = stripped[::-1]
        if stripped == rev:
            return True
        return False

obj = Solution()
ans = obj.isPalindrome("A man, a plan, a canal: Panama")
print(ans)