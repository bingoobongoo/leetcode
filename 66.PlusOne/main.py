class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        for i in range(len(digits)):
            digits[-(i+1)] += 1
            if digits[-(i+1)] > 9:
                digits[-(i+1)] = 0
            else:
                return digits
            if digits[0] == 0:
                digits.insert(0, 1)
            
        return digits