class Cell():
    def __init__(self, col, row, value):
        self.col = col
        self.row = row
        self.value = value
        self.nextHopCount = 0
        self.possibleNextHops = []
        self.nextHop = None

class Solution(object):
    def maxIncreasingCells(self, mat):
        cells = []
        for rowIdx, row in enumerate(mat):
            for colIdx, value in enumerate(row):
                cells.append(Cell(colIdx, rowIdx, value))

        maxHopCount = 0
        for cell in cells:
            for otherCell in cells:
                if (otherCell.row == cell.row or otherCell.col == cell.col) and otherCell.value > cell.value:
                    cell.nextHopCount += 1
                    cell.possibleNextHops.append(otherCell)

            if cell.nextHopCount > maxHopCount:
                maxHopCount = cell.nextHopCount

        for cell in cells:
            maxNextHopCount = 0
            minNextHopValue = 1000000
            nextHopCell = None
            for otherCell in cell.possibleNextHops:
                if otherCell.nextHopCount > maxNextHopCount:
                    maxNextHopCount = otherCell.nextHopCount
                    minNextHopValue = otherCell.value
                    nextHopCell = otherCell
                elif otherCell.nextHopCount == maxNextHopCount:
                    if otherCell.value < minNextHopValue:
                        minNextHopValue = otherCell.value
                        nextHopCell = otherCell
            cell.nextHop = nextHopCell

        moves = []
        for cell in cells:
            if cell.nextHopCount == maxHopCount:
                # print(cell.value)
                moves.append(self.maxMoves(cell))
        
        maxMoves = max(moves)
        # for cell in cells:
        #     if cell.nextHop != None:
        #         print(f'Cell: {cell.value}, NextHop: {cell.nextHop.value}')
        #     else:
        #         print(f'Cell: {cell.value}, NextHop: BRAK')
        return maxMoves

    def maxMoves(self, cell):
        if cell.nextHop == None:
            return 1
        return self.maxMoves(cell.nextHop) + 1 
    
obj = Solution()
print(f'Max moves: {obj.maxIncreasingCells([[3,1,6],[-9,5,7]])}')