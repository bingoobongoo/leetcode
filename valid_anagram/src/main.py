class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_map = {}
        for char in s:
            if hash_map.get(char) == None:
                hash_map[char] = 1
            else:
                hash_map[char] += 1
        for char in t:
            if hash_map.get(char) == None:
                return False
            else:
                if hash_map[char] == 0:
                    return False
                hash_map[char] -= 1
        for value in hash_map.values():
            if value != 0:
                return False
        
        return True

obj = Solution()
print(obj.isAnagram("anagram", "nagarm"))