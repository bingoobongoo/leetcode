class Solution:
    def isPalindrome(self, x: int) -> bool:
        string = str(x)
        backString = string[::-1]
        if string == backString:
            return True
        else:
            return False