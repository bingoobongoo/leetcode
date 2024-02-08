class Cell():
    def __init__(self, col, row, value):
        self.col = col
        self.row = row
        self.value = value
        self.possibleNextHops = []
        self.maxVisited = None

class Solution(object):
    def maxIncreasingCells(self, mat):
        cells = []
        for rowIdx, row in enumerate(mat):
            for colIdx, value in enumerate(row):
                cells.append(Cell(colIdx, rowIdx, value))

        for cell in cells:
            for otherCell in cells:
                if (otherCell.row == cell.row or otherCell.col == cell.col) and otherCell.value > cell.value:
                    cell.possibleNextHops.append(otherCell)


        moves = []
        for cell in cells:
            moves.append(self.findMaxVisited(cell))
        
        maxMoves = max(moves)
        return maxMoves

    def findMaxVisited(self, cell):
        if cell.maxVisited != None:
            return cell.maxVisited
        if len(cell.possibleNextHops) == 0:
            cell.maxVisited = 1
            return cell.maxVisited
        
        visitedValues = []
        for nextHopCell in cell.possibleNextHops:
            visitedValues.append(self.findMaxVisited(nextHopCell))
        cell.maxVisited = max(visitedValues) + 1
        return cell.maxVisited
    
obj = Solution()
print(f'Max moves: {obj.maxIncreasingCells([[3,1,6],[-9,5,7]])}')