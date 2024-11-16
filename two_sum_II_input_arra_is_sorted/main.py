class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        hash_map = {}
        for (i, num) in enumerate(numbers):
            diff = target - num
            ans_found = hash_map.get(num)
            if ans_found == None:
                hash_map[diff] = i
            else:
                return [ans_found+1, i+1]

obj = Solution()
ans = obj.twoSum([2,3,4], 6)
print(ans)