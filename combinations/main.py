class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        ans = []
        startingList = list(range(1,k+1))

        currentList = startingList
        for i in range(k-2):
            while currentList[-(i+1)] < n-i:
                ans.append(currentList)
                while currentList[-1] < n:
                    currentList[-1] += 1
                    ans.append(currentList)
                currentList[-(i+2)] += 1
                currentList[-(i+1)] = currentList[-(i+2)] + 1
            ans.append(currentList)
            currentList[-(i+3)]


myList = list(range(1,2))
print(myList)