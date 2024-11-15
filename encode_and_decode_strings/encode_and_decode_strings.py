class Solution:

    def encode(self, strs: list[str]) -> str:
        encoded_str = "#!#".join(strs)
        return encoded_str

    def decode(self, s: str) -> list[str]:
        decoded_strs = s.split("#!#")
        return decoded_strs
    
obj = Solution()
encoded = obj.encode(["neet","code","love","you"])
print(encoded)
print(obj.decode(encoded))