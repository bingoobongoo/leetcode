class Solution:
    def numberOfPairs(self, points):
        sortedPoints = sorted(points)
        counter = 0
        for aliceIdx, point in enumerate(sortedPoints):
            alicePos = point
            for otherPoint in sortedPoints[aliceIdx+1:]:
                if otherPoint[1] <= alicePos[1] and otherPoint[0] >= alicePos[0]:
                    bobPos = otherPoint
                    bobIdx = sortedPoints.index(bobPos)
                    boundaryViolated = False
                    for guestPoint in sortedPoints[:bobIdx+1]:
                        if guestPoint[1] < alicePos[1] and guestPoint[1] > bobPos[1]:
                            boundaryViolated = True
                            break
                    if not boundaryViolated:
                        counter += 1
                
                elif otherPoint[0] == alicePos[0] and otherPoint[1] > alicePos[1]:
                    bobPos = alicePos
                    bobIdx = sortedPoints.index(bobPos)
                    alicePos = otherPoint
                    boundaryViolated = False
                    for guestPoint in sortedPoints[aliceIdx:bobIdx+1]:
                        if guestPoint[1] < alicePos[1] and guestPoint[1] > bobPos[1]:
                            boundaryViolated = True
                            break
                    if not boundaryViolated:
                        counter += 1
        
        return counter
    
obj = Solution()
print(obj.numberOfPairs([[3,1], [1,3], [1,1]]))

print(sorted([[3,1], [1,3], [1,1]]))