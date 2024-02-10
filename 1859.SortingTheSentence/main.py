class Solution:
    def sortSentence(self, s: str) -> str:
        answer_list = []
        words = s.split(" ")
        for i in range(len(words)): 
            answer_list.append(0)

        for word in words:
            answer_list[int(word[-1])-1] = word[:-1]
        
        return " ".join(answer_list)

obj = Solution()
print(obj.sortSentence("Myself2 Me1 I4 and3"))