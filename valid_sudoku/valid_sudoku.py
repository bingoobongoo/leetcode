class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows_hm = [{} for i in range(9)]
        cols_hm = [{} for i in range(9)]
        squares_hm = [{} for i in range(9)]
        
        for row in list(range(9)):
            for col in list(range(9)):
                if board[row][col] == ".":
                    continue
                number = int(board[row][col])
                if number > 9 or number < 1:
                    return False
                row_num = rows_hm[row].get(number)
                if row_num == None:
                    rows_hm[row][number] = 1
                else:
                    return False

                col_num = cols_hm[col].get(number)
                if col_num == None:
                    cols_hm[col][number] = 1
                else:
                    return False
                    
                square_num = squares_hm[row//3*3 + col//3].get(number)
                if square_num == None:
                    squares_hm[row//3*3 + col//3][number] = 1
                else:
                    return False  
        print(rows_hm)
                
        return True             
        
obj = Solution()
ans = obj.isValidSudoku([["8","3",".",".","7",".",".",".","."]
                        ,["6",".",".","1","9","5",".",".","."]
                        ,[".","9","8",".",".",".",".","6","."]
                        ,["8",".",".",".","6",".",".",".","3"]
                        ,["4",".",".","8",".","3",".",".","1"]
                        ,["7",".",".",".","2",".",".",".","6"]
                        ,[".","6",".",".",".",".","2","8","."]
                        ,[".",".",".","4","1","9",".",".","5"]
                        ,[".",".",".",".","8",".",".","7","9"]])
print(ans)