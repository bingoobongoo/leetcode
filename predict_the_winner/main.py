class Solution:
    def PredictTheWinner(self, nums: list[int]) -> bool:
        rootNode = Node(True, nums)
        return solution(self, rootNode)

class Node:
    def __init__(self, turn: bool, currentNums: list[int], player1Score: int=0, player2Score: int=0) -> None:
        self.turn = turn
        self.currentNums = currentNums
        self.player1Score = player1Score
        self.player2Score = player2Score

def solution(self, node) -> bool:
    if not node.currentNums:
        if node.player1Score >= node.player2Score:
            return True
        else:
            return False
    if node.turn:
        leftNode = Node(False, node.currentNums[1:], node.player1Score + node.currentNums[0], node.player2Score)
        leftScore = solution(self, leftNode)
        if leftScore:
            return True
        rightNode = Node(False, node.currentNums[:-1], node.player1Score + node.currentNums[-1], node.player2Score)
        rightScore = solution(self, rightNode)

        if leftScore or rightScore:
            return True
        else:
            return False
    
    else:
        leftNode = Node(True, node.currentNums[1:], node.player1Score, node.player2Score + node.currentNums[0])
        leftScore = solution(self, leftNode)
        if not leftScore:
            return False
        
        rightNode = Node(True, node.currentNums[:-1], node.player1Score, node.player2Score + node.currentNums[-1])
        rightScore = solution(self, rightNode)

        if leftScore and rightScore:
            return True
        else:
            return False
        
obj = Solution()
ans = obj.PredictTheWinner([10000000,10000000,10000000,10000000,10000000,10000000,10000000,10000000,10000000,10000000,0,0,0,0,0,0,0,0,0,0])
print(ans)