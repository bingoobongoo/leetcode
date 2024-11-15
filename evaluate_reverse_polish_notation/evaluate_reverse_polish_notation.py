class Solution:
    current_tokens = []
    def __init__(self):
        self.current_tokens = []
    def evalRPN(self, tokens: list[str]) -> int:
        for token in tokens:
            self.call_stack(token)
        return int(self.current_tokens[0])
    
    def call_stack(self, token: str):
        if token in ["+", "-", "*", "/"]:
            num1 = int(self.current_tokens.pop())
            num2 = int(self.current_tokens.pop())
            if token == "+":
                self.current_tokens.append(num2 + num1)
                return
            if token == "-":
                self.current_tokens.append(num2 - num1)
                return
            if token == "*":
                self.current_tokens.append(num2 * num1)
                return
            if token == "/":
                self.current_tokens.append(int(num2 / num1))
                return
        else:
            self.current_tokens.append(token)
            return
        
obj = Solution()
ans = obj.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])