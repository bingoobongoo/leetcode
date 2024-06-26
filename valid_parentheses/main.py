class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }
        stack = []

        for bracket in s:
            if len(stack) == 0:
                stack.append(bracket)
            else:
                try:
                    if brackets[stack[-1]] == bracket:
                        stack.pop()
                    else:
                        stack.append(bracket)
                except:
                    stack.append(bracket)
        if len(stack) > 0:
            return False
        else:
            return True

obj = Solution()
ans = obj.isValid("({[)")
print(ans)