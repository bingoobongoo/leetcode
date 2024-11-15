class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hash_map = {}
        for string in strs:
            key_sorted = "".join(sorted(string))
            value = hash_map.get(key_sorted)
            if not value:
                hash_map[key_sorted] = [string]
            else:
                hash_map[key_sorted].append(string)
            
        ans = hash_map.values()
        return list(ans)

obj = Solution()
print(obj.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))