class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        triplets = []
        triples_sorted = []
        for (i, num) in enumerate(nums):
            target = -num
            nums_copy = nums
            nums_copy.pop(i)
            others = nums_copy
            hash_map = {}
            for value in others:
                diff = target - value
                x = hash_map.get(value)
                if x == None:
                    hash_map[diff] = value
                else:
                    triplet = [-target, value, x]
                    triplet_srtd = sorted(triplet)
                    if triplet_srtd in triples_sorted:
                        continue
                    else:
                        triples_sorted.append(triplet_srtd)
                        triplets.append([-target, value, x])
        triplets.sort(key=lambda y:y[0])
        return triplets
    
obj = Solution()
ans = obj.threeSum([-1,0,1,2,-1,-4])
print(ans)
