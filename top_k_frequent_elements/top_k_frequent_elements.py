class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        elem_freq = {}
        for num in nums:
            freq = elem_freq.get(num)
            if not freq:
                elem_freq[num] = 1
            else:
                elem_freq[num] += 1
        
        key_value_pairs_sorted = sorted(list(elem_freq.items()), key=lambda x : x[1], reverse=True)
        ans = [pair[0] for pair in key_value_pairs_sorted]
        return ans[:k]

obj = Solution()
print(obj.topKFrequent([1,2,2,3,3,3,4,5,5], 2))