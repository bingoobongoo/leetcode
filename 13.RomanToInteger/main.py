class Solution:
    def romanToInt(self, s: str) -> int:
        value = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }

        sum = 0
        for i in range(len(s)):
            try:
                if value[s[i+1]] > value[s[i]]:
                    sum -= value[s[i]]
                else:
                    sum += value[s[i]]
            except:
                sum += value[s[i]]
        return sum